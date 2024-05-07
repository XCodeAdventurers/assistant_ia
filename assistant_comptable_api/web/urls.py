from django.urls import path
from .views import (
    homeViews,
    accountsViews,
    operationsViews,
    assistanceView,
)

app_name="web"

urlpatterns = [
    path('', view=homeViews.home, name='home'),
    path('operations/', view=operationsViews.index, name='operations'),
    path('operations/create/', view=operationsViews.create, name='user_create'),
    path('operations/update/<int:id>/', view=operationsViews.update, name='operations_update'),
    path('operations/delete/<int:id>/', view=operationsViews.delete, name='operations_delete'),

    path('accounts/', view=accountsViews.index, name='accounts'),
    path('accounts/create/', view=accountsViews.create, name='user_create'),
    path('accounts/update/<int:id>/', view=accountsViews.update, name='accounts_update'),
    path('accounts/delete/<int:id>/', view=accountsViews.delete, name='accounts_delete'),

    path('assistance', view=assistanceView.index, name='assistance'),

]
