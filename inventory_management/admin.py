"""
Admin registration for Inventory Management models.
"""
from django.contrib import admin
from .models.warehouse import Warehouse
from .models.location import Location
from .models.stockjournal import StockJournal
from .models.product import Product
from .models.productvariant import ProductVariant
from .models.productcategory import ProductCategory
from .models.unitofmeasure import UnitOfMeasure
from .models.stockmovement import StockMovement
from .models.lotserial import LotSerial
from .models.batchtransfer import BatchTransfer
from .models.inventoryadjustment import InventoryAdjustment
from .models.stockreplenishment import StockReplenishment
from .models.stocklevel import StockLevel
from .models.stockvaluation import StockValuation
from .models.inventorywastage import InventoryWastage
from .models.gatepass import GatePass

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'manager', 'is_active')
    list_filter = ('is_active', 'manager')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'warehouse', 'parent_location')
    list_filter = ('type', 'warehouse')

@admin.register(StockJournal)
class StockJournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'source_location', 'destination_location')
    list_filter = ('type',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'sku', 'category', 'uom', 'price', 'tracking', 'is_active')
    list_filter = ('category', 'uom', 'tracking', 'is_active')
    search_fields = ('name', 'barcode', 'sku')

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute_name', 'value')
    list_filter = ('attribute_name',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)

@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'conversion_factor')
    list_filter = ('type',)

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('reference_no', 'product', 'from_location', 'to_location', 'quantity', 'movement_type', 'movement_date', 'status', 'journal')
    list_filter = ('movement_type', 'status', 'product')
    search_fields = ('reference_no',)

@admin.register(LotSerial)
class LotSerialAdmin(admin.ModelAdmin):
    list_display = ('product', 'lot_or_serial_no', 'type', 'status', 'mfg_date', 'exp_date')
    list_filter = ('type', 'status', 'product')
    search_fields = ('lot_or_serial_no',)

@admin.register(BatchTransfer)
class BatchTransferAdmin(admin.ModelAdmin):
    list_display = ('batch_reference', 'source_location', 'dest_location', 'transfer_date', 'status')
    list_filter = ('status',)

@admin.register(InventoryAdjustment)
class InventoryAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'location', 'reason', 'status', 'adjusted_by', 'adjusted_on')
    list_filter = ('status', 'reason')

@admin.register(StockReplenishment)
class StockReplenishmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'type', 'trigger_level', 'quantity')
    list_filter = ('type', 'product', 'location')

@admin.register(StockLevel)
class StockLevelAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'min_qty', 'max_qty')
    list_filter = ('product', 'location')

@admin.register(StockValuation)
class StockValuationAdmin(admin.ModelAdmin):
    list_display = ('product', 'method', 'unit_cost', 'total_quantity', 'total_value', 'date')
    list_filter = ('method', 'product')

@admin.register(InventoryWastage)
class InventoryWastageAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'reason', 'location', 'approved_by', 'wastage_date')
    list_filter = ('reason', 'location', 'approved_by')

@admin.register(GatePass)
class GatePassAdmin(admin.ModelAdmin):
    list_display = ('gate_pass_number', 'purpose', 'product', 'quantity', 'issued_to', 'issue_date', 'return_date', 'status')
    list_filter = ('purpose', 'status', 'product')
    search_fields = ('gate_pass_number',)
