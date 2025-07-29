"""
Admin registration for HRMS models.
"""
from django.contrib import admin
from .models.employee import Employee
from .models.attendancemachine import AttendanceMachine
from .models.contract import Contract
from .models.payroll import Payroll
from .models.recruitment import Recruitment
from .models.leave import Leave
from .models.attendance import Attendance
from .models.loan import Loan
from .models.allowance import Allowance
from .models.appraisal import Appraisal
from .models.tax import Tax

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'cnic', 'designation', 'department', 'status', 'join_date')
    search_fields = ('full_name', 'email', 'phone', 'cnic')
    list_filter = ('designation', 'department', 'status')

@admin.register(AttendanceMachine)
class AttendanceMachineAdmin(admin.ModelAdmin):
    list_display = ('machine_id', 'location', 'ip_address', 'connected_status')
    search_fields = ('machine_id', 'location', 'ip_address')
    list_filter = ('connected_status',)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('employee', 'contract_type', 'start_date', 'end_date', 'basic_salary', 'probation_period', 'status')
    search_fields = ('employee__full_name', 'contract_type')
    list_filter = ('contract_type', 'status')

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'gross_salary', 'deductions', 'net_salary', 'is_paid')
    search_fields = ('employee__full_name', 'month')
    list_filter = ('is_paid',)

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'position_applied', 'status')
    search_fields = ('full_name', 'email', 'phone', 'position_applied')
    list_filter = ('status',)

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'reason', 'status')
    search_fields = ('employee__full_name', 'leave_type', 'reason')
    list_filter = ('leave_type', 'status')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'clock_in', 'clock_out', 'total_hours')
    search_fields = ('employee__full_name', 'date')
    list_filter = ('date',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'reason', 'start_date', 'monthly_installment', 'remaining_amount', 'is_settled')
    search_fields = ('employee__full_name', 'reason')
    list_filter = ('is_settled',)

@admin.register(Allowance)
class AllowanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'title', 'amount', 'date_given')
    search_fields = ('employee__full_name', 'title')
    list_filter = ('date_given',)

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'remarks', 'previous_salary', 'new_salary', 'rating')
    search_fields = ('employee__full_name', 'remarks')
    list_filter = ('date', 'rating')

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'tax_percentage', 'tax_amount')
    search_fields = ('employee__full_name', 'month')
    list_filter = ('month',)
