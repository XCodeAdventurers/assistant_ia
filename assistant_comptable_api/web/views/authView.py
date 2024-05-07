
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from api.forms import PersonForm, BusinessForm

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

def custom_register(request):
    data = {}
    if request.method == "POST":
        account_plan = request.POST.get('account_plan')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            if password == confirm_password:
                print("Person is valide")
                person = person_form.save(commit=False)
                person.bind_user(password)
                if account_plan == "account_plan_business":
                    business_form = BusinessForm(request.POST)
                    pass
                login(request, user=person.user)
            else:
                data['password_errors'] = "Les mot de passe sont imcompatible."
        print(person_form.errors)
        print(account_plan)
        # return HttpResponse('Hello')
        return redirect('web:accounts')
    else:
        data['person_form'] = PersonForm()
        data['business_form'] = BusinessForm()
        data['show_silder'] = False
    return render(request, "auth/register.html", context=data)

@login_required(login_url=settings.LOGIN_URL)
def custom_logout(request):
    logout(request)
    return redirect('/login')