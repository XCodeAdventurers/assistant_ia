from rest_framework import serializers
from .models import Person, Category, AccountType, Account, Transaction, Budget, FinancialGoal

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'sexe')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ('id', 'name')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'user', 'account_type', 'account_name', 'balance')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['account_type'] = AccountTypeSerializer(instance.account_type).data
        return data

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'account', 'amount', 'transaction_type', 'category', 'document', 'label', 'date', 'budget')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['account'] = AccountSerializer(instance.account).data
        data['category'] = CategorySerializer(instance.category).data
        return data

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'user', 'category', 'amount', 'start_date', 'end_date')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data
        return data

class FinancialGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialGoal
        fields = ('id', 'user', 'goal_name', 'target_amount', 'current_amount', 'deadline')
