"""
DRF Router for Inventory Management endpoints.
"""
from rest_framework.routers import DefaultRouter
from .views.warehouse_views import WarehouseViewSet
from .views.location_views import LocationViewSet
from .views.stockjournal_views import StockJournalViewSet
from .views.product_views import ProductViewSet
from .views.productvariant_views import ProductVariantViewSet
from .views.productcategory_views import ProductCategoryViewSet
from .views.unitofmeasure_views import UnitOfMeasureViewSet
from .views.stockmovement_views import StockMovementViewSet
from .views.lotserial_views import LotSerialViewSet
from .views.batchtransfer_views import BatchTransferViewSet
from .views.inventoryadjustment_views import InventoryAdjustmentViewSet
from .views.stockreplenishment_views import StockReplenishmentViewSet
from .views.stocklevel_views import StockLevelViewSet
from .views.stockvaluation_views import StockValuationViewSet
from .views.inventorywastage_views import InventoryWastageViewSet
from .views.gatepass_views import GatePassViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'stockjournals', StockJournalViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productvariants', ProductVariantViewSet)
router.register(r'productcategories', ProductCategoryViewSet)
router.register(r'unitsofmeasure', UnitOfMeasureViewSet)
router.register(r'stockmovements', StockMovementViewSet)
router.register(r'lotserials', LotSerialViewSet)
router.register(r'batchtransfers', BatchTransferViewSet)
router.register(r'inventoryadjustments', InventoryAdjustmentViewSet)
router.register(r'stockreplenishments', StockReplenishmentViewSet)
router.register(r'stocklevels', StockLevelViewSet)
router.register(r'stockvaluations', StockValuationViewSet)
router.register(r'inventorywastages', InventoryWastageViewSet)
router.register(r'gatepasses', GatePassViewSet)

urlpatterns = router.urls
