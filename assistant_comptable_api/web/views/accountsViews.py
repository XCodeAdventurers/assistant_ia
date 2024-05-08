from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import AccountForm
from api.models import AccountCategory, AccountType, Account, Person

MODEL_MANE = "account"
ROOT_FOLDER = "accounts"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    data = {
        "title" : "Compte",
        "model_name": MODEL_MANE,
        "account_categories": AccountCategory.objects.all(),
    }
    return render(request, INDEX_PATH, context=data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = AccountForm(request.POST)
        form_is_valid = form.is_valid()
        print(form_is_valid)
        if form_is_valid:
            account = Person.save_account(form, request.user)
            account.calculate_amount()
            data['message'] = f"L'account {account} !"
        data['form_is_valid'] = form_is_valid
    else:
        form = AccountForm()
        
    accountTypes = AccountType.objects.all()
    
    context = {
        'form': form,
        'title' : "Ajouter un compte",
        'accountTypes': accountTypes,
    }    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    account = get_object_or_404(Account, pk=id)
    print(account)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        form_is_valid = form.is_valid()
        if form_is_valid:
            account = Person.save_account(form, request.user)
            account.calculate_amount()
            data['message'] = f"L'account {account} !"
        data['form_is_valid'] = form_is_valid
    else:
        form = AccountForm(instance=account)
            
    accountTypes = AccountType.objects.all()
    
    context = {
        'form': form,
        'title' : "Mettre a jour un compte",
        'accountTypes': accountTypes,
    }    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    account = get_object_or_404(Account, pk=id)
    account.delete()
    message = f"Delete message!"
    data['message'] = message
    return JsonResponse(data)


