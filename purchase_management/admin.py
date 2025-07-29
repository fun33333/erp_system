from django.contrib import admin
from purchase_management.models import (
    Vendor, Product, PriceList, Requisition, Approval, Order, GRN, Bill, Payment
)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Admin for Vendor."""
    list_display = ('id', 'name', 'email', 'phone', 'is_active')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_active',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin for Product."""
    list_display = ('id', 'name', 'sku_code', 'unit', 'is_active')
    search_fields = ('name', 'sku_code')
    list_filter = ('is_active', 'unit')

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    """Admin for PriceList."""
    list_display = ('id', 'vendor', 'product', 'price', 'valid_from', 'valid_to')
    search_fields = ('vendor__name', 'product__name')
    list_filter = ('vendor', 'product', 'valid_from', 'valid_to')

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    """Admin for Requisition."""
    list_display = ('id', 'requested_by', 'product', 'quantity', 'status', 'created_at')
    search_fields = ('product__name', 'requested_by__username')
    list_filter = ('status', 'created_at')

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    """Admin for Approval."""
    list_display = ('id', 'requisition', 'approved_by', 'status', 'approved_on')
    search_fields = ('requisition__product__name', 'approved_by__username')
    list_filter = ('status', 'approved_on')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin for Order."""
    list_display = ('id', 'requisition', 'vendor', 'order_date', 'delivery_date', 'status')
    search_fields = ('vendor__name', 'requisition__product__name')
    list_filter = ('status', 'order_date', 'delivery_date')

@admin.register(GRN)
class GRNAdmin(admin.ModelAdmin):
    """Admin for GRN."""
    list_display = ('id', 'order', 'received_by', 'received_on', 'quantity_received')
    search_fields = ('order__vendor__name', 'received_by__username')
    list_filter = ('received_on',)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    """Admin for Bill."""
    list_display = ('id', 'order', 'bill_date', 'amount', 'due_date', 'is_paid')
    search_fields = ('order__vendor__name',)
    list_filter = ('is_paid', 'bill_date', 'due_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin for Payment."""
    list_display = ('id', 'bill', 'payment_date', 'amount', 'payment_method', 'reference_no')
    search_fields = ('reference_no', 'bill__order__vendor__name')
    list_filter = ('payment_method', 'payment_date') 