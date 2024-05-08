from django.contrib import admin
from api.models import Person, AccountCategory, Business, Journal, AccountType, Account, Operation, PromptTemplate

admin.site.register(Person)
admin.site.register(Business)
admin.site.register(Journal)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(Operation)
admin.site.register(AccountCategory)
admin.site.register(PromptTemplate)

