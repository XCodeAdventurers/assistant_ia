from django import forms
from .models import Person, Category, AccountType, Account, Transaction, Budget, FinancialGoal

SELECT_CLASSE = "block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-yellow-400 focus:outline-none focus:shadow-outline-yellow dark:focus:shadow-outline-gray"
INPUT_CLASSE = "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-yellow-400 focus:outline-none focus:shadow-outline-yellow dark:text-gray-300 dark:focus:shadow-outline-gray form-input"

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'sexe')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'last_name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'email': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'phone_number': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'sexe': forms.Select(attrs={'class': INPUT_CLASSE}, choices=Person.SEXE_CHOICES),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
        }

class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user', 'account_type', 'account_name', 'balance')
        widgets = {
            'user': forms.Select(attrs={'class': SELECT_CLASSE}),
            'account_type': forms.Select(attrs={'class': SELECT_CLASSE}),
            'account_name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'balance': forms.NumberInput(attrs={'class': INPUT_CLASSE}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('user', 'account', 'amount', 'transaction_type', 'category', 'document', 'label', 'budget')
        widgets = {
            'user': forms.Select(attrs={'class': SELECT_CLASSE}),
            'account': forms.Select(attrs={'class': SELECT_CLASSE}),
            'amount': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'transaction_type': forms.Select(attrs={'class': SELECT_CLASSE}),
            'category': forms.Select(attrs={'class': SELECT_CLASSE}),
            'document': forms.FileInput(attrs={'class': INPUT_CLASSE}),
            'label': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'budget': forms.Select(attrs={'class': SELECT_CLASSE}),
        }
        
        # def clean(self):
        #     data = super().clean()
        #     amount = self.cleaned_data["amount"]
        #     budget = self.cleaned_data["budget"]
        #     print(budget)
        #     return data

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('user', 'category', 'amount', 'start_date', 'end_date', 'cloturer')
        widgets = {
            'user': forms.Select(attrs={'class': SELECT_CLASSE}),
            'category': forms.Select(attrs={'class': SELECT_CLASSE}),
            'amount': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'start_date': forms.DateInput(attrs={'class': INPUT_CLASSE, "type": "date"}),
            'end_date': forms.DateInput(attrs={'class': INPUT_CLASSE, "type": "date"}),
        }
    

class FinancialGoalForm(forms.ModelForm):
    class Meta:
        model = FinancialGoal
        fields = ('user', 'goal_name', 'target_amount', 'deadline')
        widgets = {
            'user': forms.Select(attrs={'class': SELECT_CLASSE}),
            'goal_name': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'target_amount': forms.TextInput(attrs={'class': INPUT_CLASSE}),
            'deadline': forms.DateInput(attrs={'class': INPUT_CLASSE, 'type': 'date'}),
        }
