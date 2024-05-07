from django.shortcuts import render, HttpResponse, redirect

def home(request):
    template_name = "welcome.html"
    data = {}
    return render(request, template_name, context=data)

