from rest_framework import serializers
from .models import Person, Business, Journal, AccountType, Account, Operation, PromptTemplate

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'profil', 'first_name', 'last_name', 'email', 'phone_number', 'sexe')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'localisation_gps', 'country', 'town', 'district', 'person')

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'name', 'amount', 'person', 'business')

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ('id', 'create_at', 'update_at', 'journal')

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ('id', 'name', 'debit_operation', 'credit_operation')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'number', 'name', 'description', 'account_type', 'solde', 'solde_debit', 'solde_credit')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['account_type'] = AccountTypeSerializer(instance.account_type).data
        return data

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('id', 'ref', 'amount', 'type_operation', 'libelle', 'account')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['account'] = AccountSerializer(instance.account).data
        return data

class PromptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptTemplate
        fields = ('id', 'name', 'prompt')
