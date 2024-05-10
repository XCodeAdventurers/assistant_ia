from django.contrib import admin
from api.models import Category, AccountType, Person, Account, Transaction, Budget, FinancialGoal, PromptTemplate

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Budget)
admin.site.register(FinancialGoal)
admin.site.register(PromptTemplate)

