from django.urls import path
from .views import (
    PersonAPIView, CategoryAPIView, AccountTypeAPIView,
    AccountAPIView, TransactionAPIView, BudgetAPIView, FinancialGoalAPIView
)

urlpatterns = [
    path('persons/', PersonAPIView.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonAPIView.as_view(), name='person-detail'),
    
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),
    
    path('account-types/', AccountTypeAPIView.as_view(), name='account-type-list'),
    path('account-types/<int:pk>/', AccountTypeAPIView.as_view(), name='account-type-detail'),
    
    path('accounts/', AccountAPIView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountAPIView.as_view(), name='account-detail'),
    
    path('transactions/', TransactionAPIView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionAPIView.as_view(), name='transaction-detail'),
    
    path('budgets/', BudgetAPIView.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', BudgetAPIView.as_view(), name='budget-detail'),
    
    path('goals/', FinancialGoalAPIView.as_view(), name='financial-goal-list'),
    path('goals/<int:pk>/', FinancialGoalAPIView.as_view(), name='financial-goal-detail'),
]
