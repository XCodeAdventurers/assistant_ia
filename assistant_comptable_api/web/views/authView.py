
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

def custom_login(request):
    data = {}
    if request.method == "POST":
        inputs = request.POST
        email_or_contact = inputs.get('email_or_contact')
        password = inputs.get('password')
        print(email_or_contact, password)
        if email_or_contact!="" and password!="":
            user = authenticate(request, username=email_or_contact, password=password)
            if user:
                login(request, user=user)
                return redirect('/')
        data['error'] = "Idendifiant incorrect"
    return render(request, 'auth/login.html', context=data)

@login_required(login_url=settings.LOGIN_URL)
def custom_logout(request):
    logout(request)
    return redirect('/login')