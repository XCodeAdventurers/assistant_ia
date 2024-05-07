from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    # profil = models.ImageField(upload_to="users_profils", null=True, blank=True, verbose_name="Photo de profil")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom de famille")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Adresse email")
    phone_number = models.CharField(max_length=50, unique=True, verbose_name="Numéro de téléphone")
    SEXE_CHOICES = [
        ('F', 'Féminin'),
        ('M', 'Masculin')
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, verbose_name="Sexe")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def get_role(self):
        role = self.user.groups.all()
    
    def bind_user(self, password):
        username = f"{self.last_name}{self.first_name}{Person.objects.count()+1}".lower()
        if not self.id:
            self.user = User.objects.create_user(username=username, password=password)
        self.save()        
    
    def update_user_password(self, new_password):
        pass   
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    
    def __str__(self):
        return self.get_full_name()

class Business(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom", blank=True,)
    localisation_gps = models.CharField(max_length=100, verbose_name="Localisation GPS", blank=True, default="")
    country = models.CharField(max_length=100, verbose_name="Pays", blank=True,)
    town = models.CharField(max_length=100, verbose_name="Ville", blank=True,)
    district = models.CharField(max_length=100, verbose_name="Quartier", blank=True,)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, blank=True)

class Journal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    amount = models.IntegerField(verbose_name="Montant", default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kargs):
        super().save(*args, **kargs)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    OPERATIONS = [
        ('increase', 'increase'),
        ('decrease', 'decrease')
    ] 
    
    name = models.CharField(max_length=100, verbose_name="Nom")
    debit_operation = models.CharField(max_length=15, verbose_name="Opération au débit", choices=OPERATIONS)
    credit_operation = models.CharField(max_length=15, verbose_name="Opération au crédit")
    
    def __str__(self):
        return self.name
    
class Account(models.Model):
    number = models.CharField(max_length=100, verbose_name="Numéro", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.CharField(max_length=255, verbose_name="Description")
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
   
class Operation(models.Model):
    TYPES_OPERATIONS = [
        ('débit', 'débit'),
        ('crédit', 'crédit')
    ]
    
    TYPES_OPERATIONS = [
        ('depôt', 'depôt'),
        ('retrait', 'retrait')
    ]
    
    libelle = models.CharField(max_length=255, verbose_name="Libelle")
    ref = models.CharField(max_length=100, verbose_name="Ref")
    amount = models.IntegerField(verbose_name="Montant")
    type_operation = models.CharField(max_length=10, choices=TYPES_OPERATIONS, verbose_name="Type", blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé à")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour à")
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class PromptTemplate(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nom")
    prompt = models.TextField(verbose_name="Prompte")



