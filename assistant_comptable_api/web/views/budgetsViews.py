from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import BudgetForm
from api.models import Budget, Person

MODEL_MANE = "budget"
ROOT_FOLDER = "budgets"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"

def index(request):
    data = {
        "title" : ROOT_FOLDER,
        "model_name": MODEL_MANE,
    }
    return render(request, INDEX_PATH, context=data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        form_is_valid = form.is_valid()
        if form_is_valid:
            budget = Budget.add_user_budget(form, request.user)
            data['message'] = f"Le Buget {budget} a été ajouter avec succes !"

        data['form_is_valid'] = form_is_valid
    else:
        form = BudgetForm()

    context = {
        'form': form,
        'title' : "Ajouter un buget",
    }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    budget = get_object_or_404(Budget, pk=id)
    print(budget)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        form_is_valid = form.is_valid()
        if form_is_valid:
            budget = Budget.add_user_budget(form, request.user)
            data['message'] = f"Le Buget {budget} a été mis a jours avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = BudgetForm(instance=budget)
        
    context = {
        'form': form,
        'title' : "Mettre à jour un budget",
        'budget': budget,
    }
    
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    budget = get_object_or_404(Budget, pk=id)
    budget.delete()
    message = f"Le buget {budget} a été supprimer avec succes !"
    data['message'] = message
    return JsonResponse(data)



