
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.cache import cache

from api.forms import PersonForm
from api.models import Person
from paypal.standard.forms import PayPalPaymentsForm
from cinetpay_sdk.s_d_k import Cinetpay

import uuid

def politique(request):
    return render(request, "auth/politiques.html")

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
                    return redirect('/money_tracker/')
        data['error'] = "Idendifiant incorrect"
    data['show_silder'] = True
    return render(request, 'auth/login.html', context=data)

def custom_register(request):
    data = {}
    if request.method == "POST":
        politiques = request.POST.get('politiques')
        person_form = PersonForm(request.POST)
        if politiques:
            account_plan = request.POST.get('account_plan')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if person_form.is_valid():
                if password == confirm_password:
                    print("Person is valide")
                    person = person_form.save(commit=False)
                    person.bind_user(password)
                    cache.set('user_id', person.user.id, timeout=3600)
                    #login(request, user=person.user)
                else:
                    data['password_errors'] = "Les mot de passe sont imcompatible."
                print(person_form.errors)
                print(account_plan)
                # return HttpResponse('Hello')
                return redirect('checkout')
        else:
             data['error'] = "Vous devez lire et approver les politiques de la plateforme"
        
        data['person_form'] = person_form
    else:
        data['person_form'] = PersonForm()
        data['show_silder'] = False
    return render(request, "auth/register.html", context=data)

@login_required(login_url=settings.LOGIN_URL)
def custom_logout(request):
    logout(request)
    return redirect('/login')
#sb-xyvki22120476@personal.example.com
#Q-_Dc2b'
def checkout(request):
    host = request.get_host()
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': 26,
        'item_name': "Money Tracker",
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success')}",
        'cancel_url': f"http://{host}{reverse('payment-failed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
  
    context = {
        'paypal': paypal_payment,
    }
    return render(request, 'auth/checkout.html', context=context)

def success(request):
    user_id = cache.get('user_id')
    if user_id is not None:
        try:
            user = Person.objects.get(user__id=user_id).user
            login(request, user)
            cache.delete('user_id')
            return redirect('web:accounts')
        except Exception as e:
            print(e)
            
    return HttpResponse('Success')

def errors(request):
    user_id = cache.get('user_id')
    print(user_id)
    if user_id:
        try:
            person = Person.objects.get(user__id=user_id)
            person.user.delete()
            person.delete()
        except Exception as e:
            print(e)
            cache.delete('user_id')
        return redirect('login')
    return HttpResponse('Error')

def cinet_pay_payement(request):
    host = request.get_host()
    
    apikey = "1002642126625800e02e248.50196905"
    site_id = "5871248"
    
    cinetpay = Cinetpay(apikey,site_id)

    payment_data = { 
        'amount' : 100,
        'currency' : "XOF",            
        'transaction_id' : uuid.uuid4(),  
        'description' : "Payement du forfait de Money Tracker",
        'notify_url': f"http://{host}{reverse('payment-cinet-pay-success')}",  
        'return_url': f"http://{host}{reverse('payment-cinet-pay-success')}",     
        'customer_name' : "XXXXXXXXXXXX",                              
        'customer_surname' : "XXXXXXXXXXXXX",       
    }  
    
    
    cinet_payment = cinetpay.PaymentInitialization(payment_data)
    #response = cinetpay.init_transaction(payment_data)
    print(cinet_payment)
    if cinet_payment['code'] == '201':
        payment_url = cinet_payment['data']['payment_url']
        # Rediriger l'utilisateur vers l'URL de paiement
        return HttpResponseRedirect(payment_url)
    

def cinet_pay_success(request):
    user_id = cache.get('user_id')
    if user_id is not None:
        try:
            user = Person.objects.get(user__id=user_id).user
            login(request, user)
            cache.delete('user_id')
            return redirect('web:accounts')
        except Exception as e:
            print(e)
            
    return HttpResponse('Success')

def cinet_pay_errors(request):
    user_id = cache.get('user_id')
    print(user_id)
    if user_id:
        try:
            person = Person.objects.get(user__id=user_id)
            person.user.delete()
            person.delete()
        except Exception as e:
            print(e)
            cache.delete('user_id')
        return redirect('login')
    return HttpResponse('Error')
