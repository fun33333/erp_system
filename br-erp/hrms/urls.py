"""
DRF DefaultRouter for HRMS endpoints.
"""
from rest_framework.routers import DefaultRouter
from .views.employee_views import EmployeeViewSet
from .views.attendancemachine_views import AttendanceMachineViewSet
from .views.contract_views import ContractViewSet
from .views.payroll_views import PayrollViewSet
from .views.recruitment_views import RecruitmentViewSet
from .views.leave_views import LeaveViewSet
from .views.attendance_views import AttendanceViewSet
from .views.loan_views import LoanViewSet
from .views.allowance_views import AllowanceViewSet
from .views.appraisal_views import AppraisalViewSet
from .views.tax_views import TaxViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendancemachines', AttendanceMachineViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'payrolls', PayrollViewSet)
router.register(r'recruitments', RecruitmentViewSet)
router.register(r'leaves', LeaveViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'allowances', AllowanceViewSet)
router.register(r'appraisals', AppraisalViewSet)
router.register(r'taxes', TaxViewSet)

urlpatterns = router.urls
