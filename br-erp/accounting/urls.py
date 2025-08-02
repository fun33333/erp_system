from django.urls import path
from accounting.views.invoice_views import InvoiceListCreateView, InvoiceRetrieveView
from accounting.views.payment_views import PaymentListCreateView, PaymentRetrieveView
from accounting.views.ledger_views import LedgerListCreateView, LedgerRetrieveView

urlpatterns = [
    # Invoice endpoints
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveView.as_view(), name='invoice-detail'),

    # Payment endpoints
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveView.as_view(), name='payment-detail'),

    # Ledger endpoints
    path('ledgers/', LedgerListCreateView.as_view(), name='ledger-list-create'),
    path('ledgers/<int:pk>/', LedgerRetrieveView.as_view(), name='ledger-detail'),
] 