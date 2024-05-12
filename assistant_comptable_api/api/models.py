from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom de famille")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="Adresse email")
    phone_number = models.CharField(max_length=50, unique=True, verbose_name="Numéro de téléphone")
    has_pay = models.BooleanField(default=False)
    SEXE_CHOICES = [
        ('F', 'Féminin'),
        ('M', 'Masculin')
    ]
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, verbose_name="Sexe")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def bind_user(self, password):
        username = f"{self.last_name}{self.first_name}{Person.objects.count()+1}".lower()
        if not self.id:
            self.user = User.objects.create_user(username=username, password=password)
        self.save()        

    def __str__(self):
        return self.get_full_name()

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True, blank=True)
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    
    class Meta:
        unique_together = ('user', 'account_name')
    
    def update_balance_amount(self, amount):
        self.balance += amount
        self.save()
        
    def add_user_account(form, user):
        account = form.save(commit=False)
        account.user =user
        account.save()
        return account
    
    def __str__(self):
        return self.account_name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('revenue', 'Revenue'),
        ('expense', 'Dépense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    document = models.FileField(upload_to="piece_comptable", null=True, blank=True)
    label = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    budget = models.ForeignKey('Budget', on_delete=models.SET_NULL, blank=True, null=True)

    def add_user_transaction(form, user):
        transaction = form.save(commit=False)
        transaction.category = transaction.budget.category
        transaction.user =user
        transaction.save()
        return transaction
    
    def save(self, *args, **kwargs):
        if self.transaction_type == 'expense':
            self.amount = -abs(self.amount)
        if self.id:
            old_amount = Transaction.objects.get(pk=self.id).amount*-1
            diff = old_amount - (self.amount*-1)
            self.account.update_balance_amount(diff)
        else:
            self.account.update_balance_amount(self.amount)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.account.update_balance_amount(self.amount*-1)
        super().delete(*args, **kwargs)


    def __str__(self):
        return self.label

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    cloturer = models.BooleanField(default=False, blank=True)
    
    def add_user_budget(form, user):
        budget = form.save(commit=False)
        budget.user =user
        budget.save()
        return budget
    
    def is_valid(self, amount):
        if self.cloturer:
            return False
        somme_transactions = Transaction.objects.filter(budget=self).aaggregate(models.Sum('amount'))['amount__sum'] or 0
        if somme_transactions >= self.amount:
            return False
        return True
        
    def __str__(self):
        return f"{self.category} ({self.start_date} - {self.end_date})"

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()

    def add_user_goal(form, user):
        goal = form.save(commit=False)
        goal.user =user
        goal.save()
        return goal
    
    def __str__(self):
        return self.goal_name


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Setting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.TextField()

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    content = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)


# class Business(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Nom", blank=True,)
#     localisation_gps = models.CharField(max_length=100, verbose_name="Localisation GPS", blank=True, default="")
#     country = models.CharField(max_length=100, verbose_name="Pays", blank=True,)
#     town = models.CharField(max_length=100, verbose_name="Ville", blank=True,)
#     district = models.CharField(max_length=100, verbose_name="Quartier", blank=True,)
#     person = models.OneToOneField(Person, on_delete=models.CASCADE, blank=True)

# class Journal(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Nom")
#     amount = models.IntegerField(verbose_name="Montant", default=0)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    
#     def save(self, *args, **kargs):
#         super().save(*args, **kargs)

#     def __str__(self):
#         return self.name

# class AccountType(models.Model):
#     OPERATIONS = [
#         ('increase', 'increase'),
#         ('decrease', 'decrease')
#     ] 
    
#     name = models.CharField(max_length=100, verbose_name="Nom", unique=True)
#     debit_operation = models.CharField(max_length=15, verbose_name="Opération au débit", choices=OPERATIONS)
#     credit_operation = models.CharField(max_length=15, verbose_name="Opération au crédit")
    
    
#     def get_operation(type_operation):
#         if type_operation == AccountType.OPERATIONS[0][0]:
#             return 1
#         else:
#             return -1
    
#     def __str__(self):
#         return self.name

# class PlanComptable(models.Model):
#     number = models.CharField(unique=True, max_length=100, verbose_name="Numéro", blank=True, null=True)
#     name = models.CharField(unique=True, max_length=100, verbose_name="Nom")
#     description = models.CharField(max_length=255, verbose_name="Description")
    
#     def __str__(self):
#         return f"{self.number}-{self.name}"

# class Account(models.Model):
#     number = models.CharField(max_length=100, verbose_name="Numéro", blank=True, null=True)
#     name = models.CharField(max_length=100, verbose_name="Nom")
#     description = models.CharField(max_length=255, verbose_name="Description")
#     account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, null=True, blank=True)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
#     solde = models.IntegerField(verbose_name="Solde", default=0)
#     solde_debit = models.IntegerField(verbose_name="Debit", default=0)
#     solde_credit = models.IntegerField(verbose_name="Crédit", default=0)
#     categorie = models.ForeignKey(AccountCategory, on_delete=models.SET_NULL, null=True)

#     def save(self, *args, **kargs):
#         if not self.id:
#             count = str(Account.objects.filter(person=self.person).count()+1).zfill(2)
#             self.number = f"{self.categorie.number}{count}"
#         super().save(*args, **kargs)
     
#     def calculate_amount(self):
#         operations = self.operation_set.all()
#         debit_operations = operations.filter(type_operation=Operation.TYPES_OPERATIONS[0][0])
#         credit_operations = operations.filter(type_operation=Operation.TYPES_OPERATIONS[1][0])
#         self.solde_debit = sum(operation.amount for operation in debit_operations)
#         self.solde_credit = sum(operation.amount for operation in credit_operations)
#         self.solde = self.solde_debit-self.solde_credit
#         self.save()
        
#     def __str__(self):
#         return self.name
   
# class Operation(models.Model):
#     TYPES_OPERATIONS = [
#         ('débit', 'débit'),
#         ('crédit', 'crédit')
#     ]
#     fichier = models.FileField(upload_to="piece_complatble", null=True, blank=True)
#     libelle = models.CharField(max_length=255, verbose_name="Libelle")
#     ref = models.CharField(max_length=100, verbose_name="Ref", unique=True, null=True, blank=True)
#     amount = models.IntegerField(verbose_name="Montant")
#     type_operation = models.CharField(max_length=10, choices=TYPES_OPERATIONS, verbose_name="Type", blank=True)
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé à")
#     update_at = models.DateTimeField(auto_now=True, verbose_name="Mis à jour à")
#     journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True, blank=True)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
#     def save(self, *args, **kargs):
#         # # if self.type_operation == Operation.TYPES_OPERATIONS[0][0]:
#         # #     facteur = AccountType.get_operation(self.account.account_type.debit_operation)
#         # # else:
#         # #     facteur = AccountType.get_operation(self.account.account_type.credit_operation)
#         # facteur = 1
#         # if self.type_operation == Operation.TYPES_OPERATIONS[0][0]:
#         #     self.account.solde_debit += self.amount
#         # else:
#         #     self.account.solde_credit += self.amount
#         super().save(*args, **kargs)
#         self.account.calculate_amount()
    
#     def delete(self, *args, **kargs):
#         super().delete(*args, **kargs)
#         self.account.calculate_amount()

class PromptTemplate(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    prompt = models.TextField(verbose_name="Prompte")



