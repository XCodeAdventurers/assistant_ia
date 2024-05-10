from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person, Category, AccountType, Account, Transaction, Budget, FinancialGoal
from .serializers import PersonSerializer, CategorySerializer, AccountTypeSerializer, AccountSerializer, TransactionSerializer, BudgetSerializer, FinancialGoalSerializer

class PersonAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
        else:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountTypeAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            account_type = AccountType.objects.get(pk=pk)
            serializer = AccountTypeSerializer(account_type)
        else:
            account_types = AccountType.objects.all()
            serializer = AccountTypeSerializer(account_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        account_type = AccountType.objects.get(pk=pk)
        serializer = AccountTypeSerializer(account_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account_type = AccountType.objects.get(pk=pk)
        account_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(account)
        else:
            accounts = Account.objects.filter(user=request.user)
            serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = Account.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            transaction = Transaction.objects.get(pk=pk)
            serializer = TransactionSerializer(transaction)
        else:
            account_id = request.GET.get('account')
            category_id = request.GET.get('category')

            transactions = Transaction.objects.filter(user=request.user)

            if account_id != "-1":
                transactions = transactions.filter(account__id__in=[account_id])
        
            if category_id != "-1":
                transactions = transactions.filter(category__id__in=[category_id])

            serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BudgetAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            budget = Budget.objects.get(pk=pk)
            serializer = BudgetSerializer(budget)
        else:
            budgets = Budget.objects.filter(user=request.user)
            serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FinancialGoalAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            financial_goal = FinancialGoal.objects.get(pk=pk)
            serializer = FinancialGoalSerializer(financial_goal)
        else:
            financial_goals = FinancialGoal.objects.filter(user=request.user)
            serializer = FinancialGoalSerializer(financial_goals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FinancialGoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        financial_goal = FinancialGoal.objects.get(pk=pk)
        serializer = FinancialGoalSerializer(financial_goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        financial_goal = FinancialGoal.objects.get(pk=pk)
        financial_goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

