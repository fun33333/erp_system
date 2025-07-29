from rest_framework import serializers
from .models import Account, JournalEntry, JournalEntryLine, Invoice, Payment, Expense, Tax

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate_balance(self, value):
        if self.instance and self.instance.type in ['ASSET', 'LIABILITY', 'EQUITY'] and value < 0:
            raise serializers.ValidationError('Balance cannot be negative for this account type.')
        return value

class JournalEntryLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntryLine
        fields = '__all__'

class JournalEntrySerializer(serializers.ModelSerializer):
    lines = JournalEntryLineSerializer(many=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'date', 'description', 'posted', 'lines']

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        entry = JournalEntry.objects.create(**validated_data)
        for line_data in lines_data:
            JournalEntryLine.objects.create(entry=entry, **line_data)
        return entry

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__' 