from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.forms import JournalForm
from api.models import Journal, Person, Business

MODEL_MANE = "journal"
ROOT_FOLDER = "journals"
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
        form = JournalForm(request.POST)
        form_is_valid = form.is_valid()

        if form_is_valid:
            journal = form.save(commit=False)
            journal.person = None #Person.objects.all().first()
            journal.business = Business.objects.all().first()
            journal.save()
            data['message'] = f"L'operation {journal} !"

        data['form_is_valid'] = form_is_valid
    else:
        form = JournalForm()

    context = {
        'form': form,
        'title' : "Ajouter un journal",
    }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def update(request, id):
    data = {}
    journal = get_object_or_404(Journal, pk=id)
    print(journal)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        form_is_valid = form.is_valid()
        if form_is_valid:
            journal = form.save(commit=False)
            journal.save()
            data['message'] = f"L'journal {journal} !"
        data['form_is_valid'] = form_is_valid
    else:
        form = JournalForm(instance=journal)
        
    context = {
        'form': form,
        'title' : "Ajouter une opération",
    }
    
    
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

def delete(request, id):
    data = {}
    operation = get_object_or_404(Journal, pk=id)
    operation.delete()
    message = f"Delete message!"
    data['message'] = message
    return JsonResponse(data)



