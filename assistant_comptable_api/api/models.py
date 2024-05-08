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
        role = self.user.groups.all().first()
        if role:
            return role.name
        return None
    
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
    
    def get_auth_person(user):
        return Person.objects.get(user=user)
    
    def save_account(form, user):
        account = form.save(commit=False)
        auth_person = Person.get_auth_person(user)
        if auth_person.get_role() == "account_plan_personal":
            account_type = AccountType.objects.get(name="charge")
            account.account_type = account_type
        account.person = auth_person
        account.save()
        return account
    
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
    
    name = models.CharField(max_length=100, verbose_name="Nom", unique=True)
    debit_operation = models.CharField(max_length=15, verbose_name="Opération au débit", choices=OPERATIONS)
    credit_operation = models.CharField(max_length=15, verbose_name="Opération au crédit")
    
    
    def get_operation(type_operation):
        if type_operation == AccountType.OPERATIONS[0][0]:
            return 1
        else:
            return -1
    
    def __str__(self):
        return self.name

class AccountCategory(models.Model):
    number = models.CharField(unique=True, max_length=100, verbose_name="Numéro", blank=True, null=True)
    name = models.CharField(unique=True, max_length=100, verbose_name="Nom")
    description = models.CharField(max_length=255, verbose_name="Description")
    
    def __str__(self):
        return f"{self.number}-{self.name}"

class Account(models.Model):
    number = models.CharField(max_length=100, verbose_name="Numéro", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.CharField(max_length=255, verbose_name="Description")
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    solde = models.IntegerField(verbose_name="Solde", default=0)
    solde_debit = models.IntegerField(verbose_name="Debit", default=0)
    solde_credit = models.IntegerField(verbose_name="Crédit", default=0)
    categorie = models.ForeignKey(AccountCategory, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kargs):
        if not self.id:
            count = str(Account.objects.filter(person=self.person).count()+1).zfill(2)
            self.number = f"{self.categorie.number}{count}"
        super().save(*args, **kargs)
     
    def calculate_amount(self):
        operations = self.operation_set.all()
        debit_operations = operations.filter(type_operation=Operation.TYPES_OPERATIONS[0][0])
        credit_operations = operations.filter(type_operation=Operation.TYPES_OPERATIONS[1][0])
        self.solde_debit = sum(operation.amount for operation in debit_operations)
        self.solde_credit = sum(operation.amount for operation in credit_operations)
        self.solde = self.solde_debit-self.solde_credit
        self.save()
        
    def __str__(self):
        return self.name
   
class Operation(models.Model):
    TYPES_OPERATIONS = [
        ('débit', 'débit'),
        ('crédit', 'crédit')
    ]
    fichier = models.FileField(upload_to="piece_complatble", null=True, blank=True)
    libelle = models.CharField(max_length=255, verbose_name="Libelle")
    ref = models.CharField(max_length=100, verbose_name="Ref", unique=True, null=True, blank=True)
    amount = models.IntegerField(verbose_name="Montant")
    type_operation = models.CharField(max_length=10, choices=TYPES_OPERATIONS, verbose_name="Type", blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé à")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour à")
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def save(self, *args, **kargs):
        # # if self.type_operation == Operation.TYPES_OPERATIONS[0][0]:
        # #     facteur = AccountType.get_operation(self.account.account_type.debit_operation)
        # # else:
        # #     facteur = AccountType.get_operation(self.account.account_type.credit_operation)
        # facteur = 1
        # if self.type_operation == Operation.TYPES_OPERATIONS[0][0]:
        #     self.account.solde_debit += self.amount
        # else:
        #     self.account.solde_credit += self.amount
        super().save(*args, **kargs)
        self.account.calculate_amount()
    
    def delete(self, *args, **kargs):
        super().delete(*args, **kargs)
        self.account.calculate_amount()

class PromptTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    prompt = models.TextField(verbose_name="Prompte")



