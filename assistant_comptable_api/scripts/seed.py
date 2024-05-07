
from api.models import Person, Business, Journal, AccountType, Account, Operation, PromptTemplate
from django.contrib.auth.models import User

def run():
    User.objects.exclude(username__in=["amk"]).delete()
    models = [
        Person,
        Business,
        Journal
    ]
    for m in models:
        m.objects.all().delete()
        
    data_person = [
        {
            "profil": "",
            "first_name": "Abdoul Malik",
            "last_name": "KONDI",
            "email": "abdoulmalikkondi8@gmail.com",
            "phone_number": "+22893561240",
            "sexe": "M"
        }
    ]
    
    for data in data_person:
        person = Person(**data)
        person.bind_user("", "123456789")
    
    data_business = [
        {
            "name": "KONDI GLOBAL",
            "localisation_gps": "",
            "country": "Togo",
            "town": "Sokodé",
            "district": "komah",
            "person": person,
        }
    ]
    
    for data in data_business:
        Business.objects.create(**data)
    
    data_transaction = [
        {
            "create_at": "",
            "update_at": "",
            "journal": ""
        }
    ]
    
    data_account_type = [
        {
            "name": "",
            "debit_operation": "",
            "credit_operation": ""
        }
    ]
    
    data_account = [
        {
            "number": "400",
            "name": "Client",
            "description": "",
            "account_type": ""
        }
    ]

    data_prompt_template = [
        {
            "name": "",
            "prompt": ""
        }
    ]



