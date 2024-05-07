from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import OperationForm
from api.models import Account, Journal, Operation

MODEL_MANE = "operation"
ROOT_FOLDER = "operations"
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
        form = OperationForm(request.POST)
        form_is_valid = form.is_valid()
        print(form_is_valid)
        if form_is_valid:
            operation = form.save()
            data['message'] = f"L'operation {operation} !"
        data['form_is_valid'] = form_is_valid
    else:
        form = OperationForm()
        
    accounts = Account.objects.all()
    journals = Journal.objects.all()
    type_operations = Operation.TYPES_OPERATIONS
    context = {
        'form': form,
        'title' : "Ajouter une opération",
        'accounts': accounts,
        'type_operations': type_operations,
        'journals': journals,
    }
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    operation = get_object_or_404(Operation, pk=id)
    print(operation)
    if request.method == 'POST':
        form = OperationForm(request.POST, instance=operation)
        form_is_valid = form.is_valid()
        if form_is_valid:
            operation = form.save()
            data['message'] = f"L'operation {operation} !"
        data['form_is_valid'] = form_is_valid
    else:
        form = OperationForm(instance=operation)
        
    accounts = Account.objects.all()
    journals = Journal.objects.all()
    type_operations = Operation.TYPES_OPERATIONS
    context = {
        'form': form,
        'title' : "Ajouter une opération",
        'accounts': accounts,
        'type_operations': type_operations,
        'journals': journals,
    }
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    operation = get_object_or_404(Operation, pk=id)
    operation.delete()
    message = f"Delete message!"
    data['message'] = message
    return JsonResponse(data)


