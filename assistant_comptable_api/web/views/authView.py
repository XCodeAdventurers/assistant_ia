
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from api.forms import PersonForm, BusinessForm
from api.models import Person

def custom_login(request):
    data = {}
    if request.method == "POST":
        inputs = request.POST
        email_or_contact = inputs.get('email_or_contact')
        password = inputs.get('password')
        if email_or_contact!="" and password!="":
            
            person = None
            
            try:
                person = Person.objects.get(phone_number=email_or_contact)
            except Exception as e:
                print(e)
                
            if not person:
                try:
                    person = Person.objects.get(email=email_or_contact)
                except Exception as e:
                    print(e)
            print(person)
            if person:
                user = authenticate(request, username=person.user.username, password=password)
                if user:
                    login(request, user=user)
                    return redirect('/web/accounts')
        return HttpResponse("Hello")
        data['error'] = "Idendifiant incorrect"
    data['show_silder'] = True
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