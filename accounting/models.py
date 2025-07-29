from django.db import models
from django.utils import timezone

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('ASSET', 'Asset'),
        ('LIABILITY', 'Liability'),
        ('EQUITY', 'Equity'),
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.code} - {self.name}"

class JournalEntry(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return f"Journal Entry {self.id} - {self.date.date()}"

class JournalEntryLine(models.Model):
    entry = models.ForeignKey(JournalEntry, related_name='lines', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    description = models.CharField(max_length=255, blank=True)

class Tax(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled'),
    ]
    customer = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)
    items = models.TextField()  # For simplicity, can be replaced with related model

    def __str__(self):
        return f"Invoice {self.id} - {self.customer}"

class Payment(models.Model):
    PAYMENT_TYPE = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    ]
    PAYMENT_METHOD = [
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('CARD', 'Card'),
        ('CHEQUE', 'Cheque'),
    ]
    invoice = models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.SET_NULL, related_name='payments')
    type = models.CharField(max_length=3, choices=PAYMENT_TYPE)
    date = models.DateTimeField(default=timezone.now)
    method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('TRAVEL', 'Travel'),
        ('SUPPLIES', 'Supplies'),
        ('SALARY', 'Salary'),
        ('OTHER', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    vendor = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Expense {self.id} - {self.category}"
