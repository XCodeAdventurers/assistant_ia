from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person, Business, Journal, AccountType, Account, Operation, PromptTemplate
from .serializers import PersonSerializer, BusinessSerializer, JournalSerializer, AccountTypeSerializer, AccountSerializer, OperationSerializer, PromptTemplateSerializer

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


class BusinessAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            business = Business.objects.get(pk=pk)
            serializer = BusinessSerializer(business)
        else:
            businesses = Business.objects.all()
            serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        business = Business.objects.get(pk=pk)
        serializer = BusinessSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        business = Business.objects.get(pk=pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            journal = Journal.objects.get(pk=pk)
            serializer = JournalSerializer(journal)
        else:
            journals = Journal.objects.all()
            serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journal = Journal.objects.get(pk=pk)
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class TransactionAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             transaction = Transaction.objects.get(pk=pk)
#             serializer = TransactionSerializer(transaction)
#         else:
#             transactions = Transaction.objects.all()
#             serializer = TransactionSerializer(transactions, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         transaction = Transaction.objects.get(pk=pk)
#         serializer = TransactionSerializer(transaction, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         transaction = Transaction.objects.get(pk=pk)
#         transaction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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
            accounts = Account.objects.all()
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


class OperationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            operation = Operation.objects.get(pk=pk)
            serializer = OperationSerializer(operation)
        else:
            operations = Operation.objects.all()
            serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        operation = Operation.objects.get(pk=pk)
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        #operation = Operation.objects.get(pk=pk)
        #operation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PromptTemplateAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            prompt_template = PromptTemplate.objects.get(pk=pk)
            serializer = PromptTemplateSerializer(prompt_template)
        else:
            prompt_templates = PromptTemplate.objects.all()
            serializer = PromptTemplateSerializer(prompt_templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PromptTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        prompt_template = PromptTemplate.objects.get(pk=pk)
        serializer = PromptTemplateSerializer(prompt_template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prompt_template = PromptTemplate.objects.get(pk=pk)
        prompt_template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


