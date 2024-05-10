from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import FinancialGoalForm
from api.models import FinancialGoal

MODEL_MANE = "goal"
ROOT_FOLDER = "goals"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"

def index(request):
    data = {
        "title" : "Objectifs financier",
        "model_name": MODEL_MANE,
    }
    return render(request, INDEX_PATH, context=data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = FinancialGoalForm(request.POST)
        form_is_valid = form.is_valid()
        if form_is_valid:
            objectif = FinancialGoal.add_user_goal(form, request.user)
            data['message'] = f"La objectif {objectif} a été ajouter avec succes !"

        data['form_is_valid'] = form_is_valid
    else:
        form = FinancialGoalForm()

    context = {
        'form': form,
        'title' : "Ajouter un objectif",
    }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    journal = get_object_or_404(FinancialGoal, pk=id)
    print(journal)
    if request.method == 'POST':
        form = FinancialGoalForm(request.POST, instance=journal)
        form_is_valid = form.is_valid()
        if form_is_valid:
            objectif = FinancialGoal.add_user_transaction(form, request.user)
            data['message'] = f"La objectif {objectif} a été mis a jours avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = FinancialGoalForm(instance=journal)
        
    context = {
        'form': form,
        'title' : "Mettre à jour une objectif",
    }
    
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    objectif = get_object_or_404(FinancialGoal, pk=id)
    objectif.delete()
    message = f"La {objectif} a été supprimer avec succes !"
    data['message'] = message
    return JsonResponse(data)




