from django import forms
from .models import Person, Business, Journal, AccountType, Account, Operation, PromptTemplate

SELECT_CLASSE = "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray"
INPUT_CLASSE = "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('profil', 'first_name', 'last_name', 'email', 'phone_number', 'sexe')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'localisation_gps', 'country', 'town', 'district', 'person')

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('name', 'amount', 'person', 'business')

# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ('journal', )

class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ('name', 'debit_operation', 'credit_operation')

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('number', 'name', 'description', 'account_type')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'number': forms.NumberInput(attrs={'class': INPUT_CLASSE}),
            'account_type': forms.Select(attrs={'class': SELECT_CLASSE}, choices=Operation.TYPES_OPERATIONS),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSE}),
        }
        
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('ref', 'amount', 'type_operation', 'description', 'account', 'journal')
        widgets = {
            'ref': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'amount': forms.NumberInput(attrs={'class': INPUT_CLASSE}),
            'type_operation': forms.Select(attrs={'class': SELECT_CLASSE}, choices=Operation.TYPES_OPERATIONS),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSE}),
            'account': forms.Select(attrs={'class': SELECT_CLASSE}),
            'journal': forms.Select(attrs={'class': SELECT_CLASSE}),
        }
class PromptTemplateForm(forms.ModelForm):
    class Meta:
        model = PromptTemplate
        fields = ('name', 'prompt')