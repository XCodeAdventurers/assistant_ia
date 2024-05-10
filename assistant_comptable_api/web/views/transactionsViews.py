from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import TransactionForm
from api.models import Transaction, Account, Category

MODEL_MANE = "transaction"
ROOT_FOLDER = "transactions"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"

def index(request):
    data = {
        "title" : ROOT_FOLDER,
        "model_name": MODEL_MANE,
        "accounts": Account.objects.filter(user=request.user),
        "categories": Category.objects.all()
    }
    return render(request, INDEX_PATH, context=data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        form_is_valid = form.is_valid()
        if form_is_valid:
            transaction = Transaction.add_user_transaction(form, request.user)
            data['message'] = f"La transaction {transaction} a été ajouter avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = TransactionForm()

    context = {
        'form': form,
        'title' : "Ajouter une transaction",
    }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    journal = get_object_or_404(Transaction, pk=id)
    print(journal)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=journal)
        form_is_valid = form.is_valid()
        if form_is_valid:
            transaction = Transaction.add_user_transaction(form, request.user)
            data['message'] = f"La transaction {transaction} a été mis a jours avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = TransactionForm(instance=journal)
        
    context = {
        'form': form,
        'title' : "Mettre à jour une transaction",
    }
    
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    transaction = get_object_or_404(Transaction, pk=id)
    transaction.delete()
    message = f"La {transaction} a été supprimer avec succes !"
    data['message'] = message
    return JsonResponse(data)



