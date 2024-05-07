from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.models import PromptTemplate

MODEL_MANE = "assistance"
ROOT_FOLDER = "chats"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"

def index(request):
    data = {
        "title" : "IA Assistant",
        "prompts_templates": PromptTemplate.objects.all(),
    }
    return render(request, INDEX_PATH, context=data)



