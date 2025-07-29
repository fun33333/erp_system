from django.contrib import admin
from .models import Account, JournalEntry, JournalEntryLine, Invoice, Payment, Expense, Tax
from accounting.models.invoice import Invoice
from accounting.models.payment import Payment
from accounting.models.ledger import Ledger

admin.site.register(Account)
admin.site.register(JournalEntry)
admin.site.register(JournalEntryLine)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Tax)
admin.site.register(Ledger)
