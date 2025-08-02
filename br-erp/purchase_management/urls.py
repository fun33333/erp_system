from rest_framework.routers import DefaultRouter
from purchase_management.views import (
    VendorViewSet, ProductViewSet, PriceListViewSet, RequisitionViewSet, ApprovalViewSet,
    OrderViewSet, GRNViewSet, BillViewSet, PaymentViewSet
)

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'products', ProductViewSet)
router.register(r'pricelists', PriceListViewSet)
router.register(r'requisitions', RequisitionViewSet)
router.register(r'approval', ApprovalViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'grns', GRNViewSet)
router.register(r'bills', BillViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls 