from django.urls import path
from .views import (
    homeViews,
    accountsViews,
    budgetsViews,
    transactionsViews,
    goalViews,
    assistanceView,
)

app_name="web"

urlpatterns = [
    path('', view=homeViews.dashboard, name='dashboard'),

    path('accounts/', view=accountsViews.index, name='accounts'),
    path('accounts/create/', view=accountsViews.create, name='account_create'),
    path('accounts/update/<int:id>/', view=accountsViews.update, name='account_update'),
    path('accounts/delete/<int:id>/', view=accountsViews.delete, name='account_delete'),

    path('budgets/', view=budgetsViews.index, name='budgets'),
    path('budgets/create/', view=budgetsViews.create, name='budget_create'),
    path('budgets/update/<int:id>/', view=budgetsViews.update, name='budget_update'),
    path('budgets/delete/<int:id>/', view=budgetsViews.delete, name='budget_delete'),

    path('transactions/', view=transactionsViews.index, name='transactions'),
    path('transactions/create/', view=transactionsViews.create, name='transaction_create'),
    path('transactions/update/<int:id>/', view=transactionsViews.update, name='transaction_update'),
    path('transactions/delete/<int:id>/', view=transactionsViews.delete, name='transaction_delete'),

    path('goals/', view=goalViews.index, name='goals'),
    path('goals/create/', view=goalViews.create, name='goal_create'),
    path('goals/update/<int:id>/', view=goalViews.update, name='goal_update'),
    path('goals/delete/<int:id>/', view=goalViews.delete, name='goal_delete'),

    path('assistance', view=assistanceView.index, name='assistance'),
    path('stream/', assistanceView.streamView, name='stream_view'),
]

