
from api.models import Person, Account, Category, AccountType, PromptTemplate
from django.contrib.auth.models import User, Group

def run():
    User.objects.exclude(username__in=["amk"]).delete()
    models = [
        Person,
        Account,
        AccountType,
        Category
    ]
    for m in models:
        m.objects.all().delete()
        

    data_person = [
        {
            "first_name": "Abdoul Malik",
            "last_name": "KONDI",
            "email": "abdoulmalikkondi8@gmail.com",
            "phone_number": "93561240",
            "sexe": "M"
        },
        {
            "first_name": "Abdoul Malik",
            "last_name": "KONDI",
            "email": "abdoulmalikkondi9@gmail.com",
            "phone_number": "98271314",
            "sexe": "M"
        }
    ]
    
    for data in data_person:
        person = Person(**data)
        person.bind_user("123456789")
        

    categories = [
        ("Alimentation 🍲"),
        ("Logement 🏠"),
        ("Transport 🚗"),
        ("Divertissement 🎮"),
        ("Santé 💊"),
        ("Éducation 📚"),
        ("Vêtements 👕"),
        ("Voyages ✈️"),
        ("Factures 📄"),
        ("Épargne 💰"),
        ("Electricité 💡"),
        ("Eau 💧"),
        ("Salaire 💵"),
        ("Revenus locatifs 🏠"),
        ("Investissements 💼"),
        ("Bourses 📈"),
        ("Ventes en ligne 🛍️"),
        ("Prime 💼"),
        ("Autres revenus 💰")
    ]


    for category_name in categories:
        Category.objects.get_or_create(name=category_name)

    account_types = [
        ("Compte courant 💳"),
        ("Épargne 💰"),
        ("Carte de crédit 💳"),
        ("Caisse 💼"),
    ]
    
    for account_type_name in account_types:
        AccountType.objects.get_or_create(name=account_type_name)

