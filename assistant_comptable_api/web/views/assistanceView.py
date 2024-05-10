from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from api.models import PromptTemplate
from django.views.generic import View
from pypdf import PdfReader 
from django.conf import settings


MODEL_MANE = "assistance"
ROOT_FOLDER = "chats"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/partial_form_modal_add.html"
# MODEL = settings.MODEL

def load_pre_context():
    result_path = settings.BASE_DIR / "media/documents/plan_comptable_syscoada.txt"
    with open(result_path, 'r') as f:
        pre_context = f.read()
    return pre_context

# PRE_CONTEXT = load_pre_context()



def index(request):
    # print(PRE_CONTEXT)
    data = {
        "title" : "IA Assistant",
        "prompts_templates": PromptTemplate.objects.all(),
    }
    return render(request, INDEX_PATH, context=data)

def streamView(request):
    def stream_response(message):
        # response = MODEL.generate_content([f"{message} (La réponse doit être au format html.)"], stream=True)
        # for chunk in response:
        #     yield chunk.text + '\n'
        yield "**Hello guys**"
            
    if request.method == "POST":
        message = request.POST.get("message")
    else:
        message = ""
    
    return StreamingHttpResponse(stream_response(message), content_type='text/plain; charset=utf-8')




