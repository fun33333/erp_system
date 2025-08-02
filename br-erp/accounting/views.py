from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Account, JournalEntry, JournalEntryLine, Invoice, Payment, Expense, Tax
from .serializers import (
    AccountSerializer, JournalEntrySerializer, JournalEntryLineSerializer,
    InvoiceSerializer, PaymentSerializer, ExpenseSerializer, TaxSerializer
)
from django.db.models import Sum, Q
from django.utils import timezone

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

    @action(detail=False, methods=['post'])
    def post_entry(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @action(detail=True, methods=['post'])
    def generate(self, request, pk=None):
        invoice = self.get_object()
        invoice.status = 'SENT'
        invoice.save()
        return Response({'status': 'Invoice sent'}, status=status.HTTP_200_OK)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

from rest_framework.views import APIView

class GeneralLedgerView(APIView):
    def get(self, request):
        account_id = request.query_params.get('account')
        entries = JournalEntryLine.objects.all()
        if account_id:
            entries = entries.filter(account_id=account_id)
        data = JournalEntryLineSerializer(entries, many=True).data
        return Response(data)

class ProfitLossView(APIView):
    def get(self, request):
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        q = Q()
        if start:
            q &= Q(date__gte=start)
        if end:
            q &= Q(date__lte=end)
        income = Account.objects.filter(type='INCOME').aggregate(total=Sum('balance'))['total'] or 0
        expense = Account.objects.filter(type='EXPENSE').aggregate(total=Sum('balance'))['total'] or 0
        return Response({'income': income, 'expense': expense, 'profit_loss': income - expense})
