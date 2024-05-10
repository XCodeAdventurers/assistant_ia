from datetime import date
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Sum
from api.models import Transaction, Budget, Category

def home(request):
    if request.user.is_authenticated:
        return redirect('web:accounts')
    template_name = "welcome.html"
    data = {}
    return render(request, template_name, context=data)

def dashboard(request):
    template_name = "dashboard.html"
    start_date_str = request.GET.get("start_date")
    end_date_str = request.GET.get("end_date")
    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    else:
        start_date = datetime.now()
        
    if end_date_str:
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    else:
        end_date = datetime.now()

    # Répartition des dépenses par catégorie
    categories = Category.objects.all()
    expenses_by_category = []
    for category in categories:
        total_expenses = Transaction.objects.filter(category=category, user=request.user, date__range=(start_date, end_date)).aggregate(total=Sum('amount'))['total'] or 0
        expenses_by_category.append({'category': category.name, 'total_expenses': total_expenses})

    # Évolution des dépenses au fil du temps
    # Supposons que nous affichons les dépenses par mois entre deux dates données
    
    monthly_expenses = Transaction.objects.filter(date__range=(start_date, end_date), user=request.user).values('date__month').annotate(total=Sum('amount'))
    
    # Comparaison des revenus et des dépenses
    # Supposons que nous affichons les revenus et les dépenses par mois pour l'année en cours
    monthly_income = Transaction.objects.filter(transaction_type='revenue', date__year__range=(start_date.year, end_date.year), user=request.user).values('date__month').annotate(total=Sum('amount'))
    monthly_expenses_comparison = Transaction.objects.filter(transaction_type='dépense', date__year__range=(start_date.year, end_date.year), user=request.user).values('date__month').annotate(total=Sum('amount'))

    # Évolution de l'épargne au fil du temps
    # Supposons que nous affichons l'évolution du solde des comptes d'épargne par mois pour l'année en cours
    savings_balance = []

    # Comparaison des dépenses avec les budgets fixés
    budgets = Budget.objects.filter(user=request.user)
    expenses_vs_budgets = []
    for budget in budgets:
        total_expenses_for_budget = Transaction.objects.filter(category=budget.category, date__range=(start_date, end_date), user=request.user).aggregate(total=Sum('amount'))['total'] or 0
        expenses_vs_budgets.append({'budget_name': budget.category.name, 'budget_amount': budget.amount, 'total_expenses': total_expenses_for_budget})

    context = {
        'title': 'Tableau de bord',
        'expenses_by_category': expenses_by_category,
        'monthly_expenses': monthly_expenses,
        'monthly_income': monthly_income,
        'monthly_expenses_comparison': monthly_expenses_comparison,
        'savings_balance': savings_balance,
        'expenses_vs_budgets': expenses_vs_budgets,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, template_name, context)

def print_stats(request):
    pass