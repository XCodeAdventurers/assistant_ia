
from api.models import Person, Business, Journal, AccountType, Account, Operation, PromptTemplate
from django.contrib.auth.models import User, Group

def run():
    User.objects.exclude(username__in=["amk"]).delete()
    models = [
        Person,
        Business,
        Journal,
        Account,
        AccountType,
    ]
    for m in models:
        m.objects.all().delete()
    
    # Créer les groupes 
    account_plan_business, _ = Group.objects.get_or_create(name="account_plan_business")
    account_plan_personal, _ = Group.objects.get_or_create(name="account_plan_personal")
    
    
    #Créer les types de compte
    AccountType.objects.create(name="produit", debit_operation=AccountType.OPERATIONS[1][0], credit_operation=AccountType.OPERATIONS[0][0])
    AccountType.objects.create(name="charge", debit_operation=AccountType.OPERATIONS[0][0], credit_operation=AccountType.OPERATIONS[1][0])
    AccountType.objects.create(name="actif", debit_operation=AccountType.OPERATIONS[0][0], credit_operation=AccountType.OPERATIONS[1][0])
    AccountType.objects.create(name="passif", debit_operation=AccountType.OPERATIONS[1][0], credit_operation=AccountType.OPERATIONS[0][0])

    

    data_person = [
        {
            "first_name": "Abdoul Malik",
            "last_name": "KONDI",
            "email": "abdoulmalikkondi8@gmail.com",
            "phone_number": "+22893561240",
            "sexe": "M"
        }
    ]
    
    for data in data_person:
        person = Person(**data)
        person.bind_user("123456789")
        person.user.groups.add(account_plan_personal)
    
    # data_business = [
    #     {
    #         "name": "KONDI GLOBAL",
    #         "localisation_gps": "",
    #         "country": "Togo",
    #         "town": "Sokodé",
    #         "district": "komah",
    #         "person": person,
    #     }
    # ]
    
    # for data in data_business:
    #     Business.objects.create(**data)
    
    
