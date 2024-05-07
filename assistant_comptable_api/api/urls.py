from django.urls import path
from .views import (
    PersonAPIView,
    BusinessAPIView,
    JournalAPIView,
    AccountTypeAPIView,
    AccountAPIView,
    OperationAPIView,
    PromptTemplateAPIView,
)

urlpatterns = [
    path('persons/', PersonAPIView.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonAPIView.as_view(), name='person-detail'),
    path('businesses/', BusinessAPIView.as_view(), name='business-list'),
    path('businesses/<int:pk>/', BusinessAPIView.as_view(), name='business-detail'),
    path('journals/', JournalAPIView.as_view(), name='journal-list'),
    path('journals/<int:pk>/', JournalAPIView.as_view(), name='journal-detail'),
    # path('transactions/', TransactionAPIView.as_view(), name='transaction-list'),
    # path('transactions/<int:pk>/', TransactionAPIView.as_view(), name='transaction-detail'),
    path('account-types/', AccountTypeAPIView.as_view(), name='account-type-list'),
    path('account-types/<int:pk>/', AccountTypeAPIView.as_view(), name='account-type-detail'),
    path('accounts/', AccountAPIView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountAPIView.as_view(), name='account-detail'),
    path('operations/', OperationAPIView.as_view(), name='operation-list'),
    path('operations/<int:pk>/', OperationAPIView.as_view(), name='operation-detail'),
    path('prompt-templates/', PromptTemplateAPIView.as_view(), name='prompt-template-list'),
    path('prompt-templates/<int:pk>/', PromptTemplateAPIView.as_view(), name='prompt-template-detail'),
]
