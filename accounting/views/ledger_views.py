from rest_framework import generics
from accounting.models.ledger import Ledger
from accounting.serializers.ledger_serializer import LedgerSerializer

class LedgerListCreateView(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

class LedgerRetrieveView(generics.RetrieveAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer 