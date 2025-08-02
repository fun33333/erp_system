"use client"

import { useEffect, useState } from "react"
import {
  Users,
  UserPlus,
  Clock,
  DollarSign,
  FileText,
  Bell,
  CheckCircle,
  Building,
  Settings,
  Search,
  Plus,
  ChevronDown,
  RefreshCw,
  Calculator,
  TrendingUp,
  TrendingDown,
  CreditCard,
  Receipt,
  PieChart,
  BarChart3,
  AlertTriangle,
  Target,
  Wallet,
  FileSpreadsheet,
  Download,
} from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Input } from "@/components/ui/input"
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger, DialogFooter } from "@/components/ui/dialog"
import { Label } from "@/components/ui/label"
import { toast } from "@/components/ui/use-toast"

// Types
interface Employee {
  id: string
  name: string
  email: string
  department: string
  position: string
  status: "active" | "inactive"
  joinDate: string
  salary: number
  avatar?: string
}

interface Invoice {
  id: string
  invoiceNumber: string
  clientName: string
  amount: number
  status: "paid" | "unpaid" | "overdue"
  dueDate: string
  issueDate: string
}

interface Payment {
  id: string
  type: "incoming" | "outgoing"
  amount: number
  method: "cash" | "bank" | "card" | "cheque"
  status: "pending" | "completed"
  date: string
  description: string
}

interface JournalEntry {
  id: string
  date: string
  type: "sales" | "purchase" | "cash" | "bank"
  description: string
  debit: number
  credit: number
  reference: string
}

interface BankAccount {
  id: string
  name: string
  balance: number
  lastReconciled: string
  unmatchedTransactions: number
}

export default function Dashboard() {
  const [currentTime, setCurrentTime] = useState(new Date())
  const [selectedDepartment, setSelectedDepartment] = useState("hrms")
  const [selectedDateRange, setSelectedDateRange] = useState("thisMonth")
  const [searchQuery, setSearchQuery] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  // Modal states
  const [showAddEmployee, setShowAddEmployee] = useState(false)
  const [showCreateInvoice, setShowCreateInvoice] = useState(false)
  const [showRecordPayment, setShowRecordPayment] = useState(false)
  const [showJournalEntry, setShowJournalEntry] = useState(false)
  const [showNotifications, setShowNotifications] = useState(false)

  // HRMS Data
  const [employees, setEmployees] = useState<Employee[]>([
    {
      id: "1",
      name: "John Doe",
      email: "john.doe@company.com",
      department: "Engineering",
      position: "Senior Developer",
      status: "active",
      joinDate: "2023-01-15",
      salary: 75000,
      avatar: "/placeholder.svg?height=40&width=40",
    },
    {
      id: "2",
      name: "Sarah Wilson",
      email: "sarah.wilson@company.com",
      department: "Marketing",
      position: "Marketing Manager",
      status: "active",
      joinDate: "2022-08-20",
      salary: 65000,
      avatar: "/placeholder.svg?height=40&width=40",
    },
    {
      id: "3",
      name: "Mike Johnson",
      email: "mike.johnson@company.com",
      department: "Accounting",
      position: "Senior Accountant",
      status: "active",
      joinDate: "2023-03-10",
      salary: 60000,
      avatar: "/placeholder.svg?height=40&width=40",
    },
  ])

  // Accounting Data
  const [invoices, setInvoices] = useState<Invoice[]>([
    {
      id: "1",
      invoiceNumber: "INV-2024-001",
      clientName: "ABC Corp",
      amount: 15000,
      status: "unpaid",
      dueDate: "2024-02-15",
      issueDate: "2024-01-15",
    },
    {
      id: "2",
      invoiceNumber: "INV-2024-002",
      clientName: "XYZ Ltd",
      amount: 8500,
      status: "overdue",
      dueDate: "2024-01-30",
      issueDate: "2024-01-01",
    },
    {
      id: "3",
      invoiceNumber: "INV-2024-003",
      clientName: "Tech Solutions",
      amount: 12000,
      status: "paid",
      dueDate: "2024-02-20",
      issueDate: "2024-01-20",
    },
  ])

  const [payments, setPayments] = useState<Payment[]>([
    {
      id: "1",
      type: "incoming",
      amount: 12000,
      method: "bank",
      status: "completed",
      date: "2024-01-25",
      description: "Payment from Tech Solutions",
    },
    {
      id: "2",
      type: "outgoing",
      amount: 5000,
      method: "bank",
      status: "pending",
      date: "2024-01-26",
      description: "Office rent payment",
    },
    {
      id: "3",
      type: "incoming",
      amount: 3500,
      method: "cash",
      status: "completed",
      date: "2024-01-24",
      description: "Cash sale",
    },
  ])

  const [journalEntries, setJournalEntries] = useState<JournalEntry[]>([
    {
      id: "1",
      date: "2024-01-25",
      type: "sales",
      description: "Sales revenue",
      debit: 12000,
      credit: 0,
      reference: "INV-2024-003",
    },
    {
      id: "2",
      date: "2024-01-24",
      type: "cash",
      description: "Cash sale",
      debit: 3500,
      credit: 0,
      reference: "CASH-001",
    },
  ])

  const [bankAccounts, setBankAccounts] = useState<BankAccount[]>([
    {
      id: "1",
      name: "Main Business Account",
      balance: 125000,
      lastReconciled: "2024-01-20",
      unmatchedTransactions: 3,
    },
    {
      id: "2",
      name: "Petty Cash Account",
      balance: 5000,
      lastReconciled: "2024-01-25",
      unmatchedTransactions: 0,
    },
  ])

  // Financial Summary Data
  const [financialData, setFinancialData] = useState({
    revenue: 245000,
    expenses: 180000,
    profit: 65000,
    cashFlow: 45000,
    unpaidInvoices: 23500,
    overdueInvoices: 8500,
    pendingPayments: 15000,
    taxesDue: 12000,
  })

  // Form states
  const [newEmployee, setNewEmployee] = useState({
    name: "",
    email: "",
    department: "",
    position: "",
    salary: "",
    joinDate: "",
  })

  const [newInvoice, setNewInvoice] = useState({
    clientName: "",
    amount: "",
    dueDate: "",
    description: "",
  })

  const [newPayment, setNewPayment] = useState({
    type: "incoming" as "incoming" | "outgoing",
    amount: "",
    method: "bank" as "cash" | "bank" | "card" | "cheque",
    description: "",
  })

  const [newJournal, setNewJournal] = useState({
    type: "sales" as "sales" | "purchase" | "cash" | "bank",
    description: "",
    debit: "",
    credit: "",
    reference: "",
  })

  // Update time
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date())
    }, 1000)
    return () => clearInterval(interval)
  }, [])

  // Computed values
  const totalEmployees = employees.length
  const accountingEmployees = employees.filter((emp) => emp.department === "Accounting").length
  const totalPayroll = employees.reduce((sum, emp) => sum + emp.salary, 0)
  const unpaidInvoicesCount = invoices.filter((inv) => inv.status === "unpaid").length
  const overdueInvoicesCount = invoices.filter((inv) => inv.status === "overdue").length
  const pendingPaymentsCount = payments.filter((pay) => pay.status === "pending").length

  // Handlers
  const handleDepartmentSwitch = (dept: string) => {
    setSelectedDepartment(dept)
    toast({
      title: "Dashboard Switched",
      description: `Switched to ${dept === "hrms" ? "HRMS" : "Accounting"} dashboard`,
    })
  }

  const handleAddEmployee = async () => {
    if (!newEmployee.name || !newEmployee.email || !newEmployee.department) {
      toast({
        title: "Error",
        description: "Please fill in all required fields",
        variant: "destructive",
      })
      return
    }

    setIsLoading(true)
    await new Promise((resolve) => setTimeout(resolve, 1000))

    const employee: Employee = {
      id: Date.now().toString(),
      ...newEmployee,
      salary: Number.parseFloat(newEmployee.salary) || 0,
      status: "active",
      avatar: "/placeholder.svg?height=40&width=40",
    }

    setEmployees((prev) => [...prev, employee])
    setNewEmployee({ name: "", email: "", department: "", position: "", salary: "", joinDate: "" })
    setShowAddEmployee(false)
    setIsLoading(false)

    toast({
      title: "Success",
      description: `Employee ${employee.name} has been added successfully`,
    })
  }

  const handleCreateInvoice = async () => {
    if (!newInvoice.clientName || !newInvoice.amount) {
      toast({
        title: "Error",
        description: "Please fill in all required fields",
        variant: "destructive",
      })
      return
    }

    setIsLoading(true)
    await new Promise((resolve) => setTimeout(resolve, 1000))

    const invoice: Invoice = {
      id: Date.now().toString(),
      invoiceNumber: `INV-2024-${String(invoices.length + 1).padStart(3, "0")}`,
      clientName: newInvoice.clientName,
      amount: Number.parseFloat(newInvoice.amount),
      status: "unpaid",
      dueDate: newInvoice.dueDate,
      issueDate: new Date().toISOString().split("T")[0],
    }

    setInvoices((prev) => [...prev, invoice])
    setFinancialData((prev) => ({ ...prev, revenue: prev.revenue + invoice.amount }))
    setNewInvoice({ clientName: "", amount: "", dueDate: "", description: "" })
    setShowCreateInvoice(false)
    setIsLoading(false)

    toast({
      title: "Success",
      description: `Invoice ${invoice.invoiceNumber} created successfully`,
    })
  }

  const handleRecordPayment = async () => {
    if (!newPayment.amount || !newPayment.description) {
      toast({
        title: "Error",
        description: "Please fill in all required fields",
        variant: "destructive",
      })
      return
    }

    setIsLoading(true)
    await new Promise((resolve) => setTimeout(resolve, 1000))

    const payment: Payment = {
      id: Date.now().toString(),
      ...newPayment,
      amount: Number.parseFloat(newPayment.amount),
      status: "completed",
      date: new Date().toISOString().split("T")[0],
    }

    setPayments((prev) => [...prev, payment])
    setNewPayment({ type: "incoming", amount: "", method: "bank", description: "" })
    setShowRecordPayment(false)
    setIsLoading(false)

    toast({
      title: "Success",
      description: "Payment recorded successfully",
    })
  }

  const handleAddJournalEntry = async () => {
    if (!newJournal.description || (!newJournal.debit && !newJournal.credit)) {
      toast({
        title: "Error",
        description: "Please fill in all required fields",
        variant: "destructive",
      })
      return
    }

    setIsLoading(true)
    await new Promise((resolve) => setTimeout(resolve, 1000))

    const journal: JournalEntry = {
      id: Date.now().toString(),
      date: new Date().toISOString().split("T")[0],
      type: newJournal.type,
      description: newJournal.description,
      debit: Number.parseFloat(newJournal.debit) || 0,
      credit: Number.parseFloat(newJournal.credit) || 0,
      reference: newJournal.reference,
    }

    setJournalEntries((prev) => [...prev, journal])
    setNewJournal({ type: "sales", description: "", debit: "", credit: "", reference: "" })
    setShowJournalEntry(false)
    setIsLoading(false)

    toast({
      title: "Success",
      description: "Journal entry added successfully",
    })
  }

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString("en-US", {
      hour12: true,
      hour: "2-digit",
      minute: "2-digit",
    })
  }

  const formatDate = (date: Date) => {
    return date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    })
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
    }).format(amount)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              {selectedDepartment === "accounting" ? (
                <Calculator className="h-8 w-8 text-green-600" />
              ) : (
                <Building className="h-8 w-8 text-blue-600" />
              )}
              <div>
                <h1 className="text-xl font-bold text-gray-900">
                  {selectedDepartment === "accounting" ? "Accounting Dashboard" : "HRMS Dashboard"}
                </h1>
                <p className="text-sm text-gray-500">
                  {selectedDepartment === "accounting"
                    ? "Financial Management System"
                    : "Human Resource Management System"}
                </p>
              </div>
            </div>

            {/* Department Switcher */}
            <div className="flex items-center space-x-2 ml-8">
              <Button
                variant={selectedDepartment === "hrms" ? "default" : "outline"}
                size="sm"
                onClick={() => handleDepartmentSwitch("hrms")}
                className="flex items-center space-x-1"
              >
                <Users className="h-4 w-4" />
                <span>HRMS</span>
              </Button>
              <Button
                variant={selectedDepartment === "accounting" ? "default" : "outline"}
                size="sm"
                onClick={() => handleDepartmentSwitch("accounting")}
                className="flex items-center space-x-1"
              >
                <Calculator className="h-4 w-4" />
                <span>Accounting</span>
              </Button>
            </div>
          </div>

          <div className="flex items-center space-x-4">
            {/* Search */}
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
              <Input
                type="text"
                placeholder={selectedDepartment === "accounting" ? "Search transactions..." : "Search employees..."}
                className="pl-10 w-64"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>

            {/* Date Range Filter */}
            <Select value={selectedDateRange} onValueChange={setSelectedDateRange}>
              <SelectTrigger className="w-32">
                <SelectValue placeholder="Period" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="today">Today</SelectItem>
                <SelectItem value="thisWeek">This Week</SelectItem>
                <SelectItem value="thisMonth">This Month</SelectItem>
                <SelectItem value="thisYear">This Year</SelectItem>
              </SelectContent>
            </Select>

            {/* Refresh Button */}
            <Button variant="outline" size="icon" disabled={isLoading}>
              <RefreshCw className={`h-4 w-4 ${isLoading ? "animate-spin" : ""}`} />
            </Button>

            {/* Notifications */}
            <Button variant="outline" size="icon" className="relative bg-transparent">
              <Bell className="h-4 w-4" />
              <span className="absolute -top-1 -right-1 h-3 w-3 bg-red-500 rounded-full text-xs text-white flex items-center justify-center">
                3
              </span>
            </Button>

            {/* User Profile */}
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="flex items-center space-x-2">
                  <Avatar className="h-8 w-8">
                    <AvatarImage src="/placeholder.svg?height=32&width=32" alt="Admin" />
                    <AvatarFallback>AD</AvatarFallback>
                  </Avatar>
                  <span className="text-sm font-medium">Admin User</span>
                  <ChevronDown className="h-4 w-4" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end">
                <DropdownMenuItem>Profile</DropdownMenuItem>
                <DropdownMenuItem>Settings</DropdownMenuItem>
                <DropdownMenuItem>Logout</DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </header>

      <div className="p-6">
        {selectedDepartment === "hrms" ? (
          // HRMS Dashboard
          <>
            {/* HRMS Quick Stats */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
              <StatCard
                title="Total Employees"
                value={totalEmployees.toString()}
                change="+2.5%"
                changeType="positive"
                icon={Users}
                color="blue"
              />
              <StatCard
                title="Accounting Staff"
                value={accountingEmployees.toString()}
                change="+1"
                changeType="positive"
                icon={Calculator}
                color="green"
              />
              <StatCard
                title="Total Payroll"
                value={formatCurrency(totalPayroll)}
                change="+5.2%"
                changeType="positive"
                icon={DollarSign}
                color="orange"
              />
              <StatCard
                title="Active Positions"
                value="27"
                change="+3"
                changeType="positive"
                icon={CheckCircle}
                color="purple"
              />
            </div>

            <div className="grid grid-cols-12 gap-6">
              {/* HRMS Left Column */}
              <div className="col-span-12 lg:col-span-8">
                {/* Employee Overview */}
                <Card className="mb-6">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="flex items-center">
                        <Users className="mr-2 h-5 w-5 text-blue-600" />
                        Employee Overview
                      </CardTitle>
                      <Dialog open={showAddEmployee} onOpenChange={setShowAddEmployee}>
                        <DialogTrigger asChild>
                          <Button>
                            <Plus className="mr-2 h-4 w-4" />
                            Add Employee
                          </Button>
                        </DialogTrigger>
                        <DialogContent>
                          <DialogHeader>
                            <DialogTitle>Add New Employee</DialogTitle>
                          </DialogHeader>
                          <div className="space-y-4">
                            <div>
                              <Label htmlFor="name">Full Name *</Label>
                              <Input
                                id="name"
                                value={newEmployee.name}
                                onChange={(e) => setNewEmployee((prev) => ({ ...prev, name: e.target.value }))}
                                placeholder="Enter full name"
                              />
                            </div>
                            <div>
                              <Label htmlFor="email">Email *</Label>
                              <Input
                                id="email"
                                type="email"
                                value={newEmployee.email}
                                onChange={(e) => setNewEmployee((prev) => ({ ...prev, email: e.target.value }))}
                                placeholder="Enter email address"
                              />
                            </div>
                            <div>
                              <Label htmlFor="department">Department *</Label>
                              <Select
                                value={newEmployee.department}
                                onValueChange={(value) => setNewEmployee((prev) => ({ ...prev, department: value }))}
                              >
                                <SelectTrigger>
                                  <SelectValue placeholder="Select department" />
                                </SelectTrigger>
                                <SelectContent>
                                  <SelectItem value="Engineering">Engineering</SelectItem>
                                  <SelectItem value="Sales">Sales</SelectItem>
                                  <SelectItem value="Marketing">Marketing</SelectItem>
                                  <SelectItem value="Accounting">Accounting</SelectItem>
                                  <SelectItem value="HR">HR</SelectItem>
                                  <SelectItem value="Finance">Finance</SelectItem>
                                </SelectContent>
                              </Select>
                            </div>
                            <div>
                              <Label htmlFor="position">Position</Label>
                              <Input
                                id="position"
                                value={newEmployee.position}
                                onChange={(e) => setNewEmployee((prev) => ({ ...prev, position: e.target.value }))}
                                placeholder="Enter position"
                              />
                            </div>
                            <div>
                              <Label htmlFor="salary">Annual Salary</Label>
                              <Input
                                id="salary"
                                type="number"
                                value={newEmployee.salary}
                                onChange={(e) => setNewEmployee((prev) => ({ ...prev, salary: e.target.value }))}
                                placeholder="Enter annual salary"
                              />
                            </div>
                            <div>
                              <Label htmlFor="joinDate">Join Date</Label>
                              <Input
                                id="joinDate"
                                type="date"
                                value={newEmployee.joinDate}
                                onChange={(e) => setNewEmployee((prev) => ({ ...prev, joinDate: e.target.value }))}
                              />
                            </div>
                          </div>
                          <DialogFooter>
                            <Button variant="outline" onClick={() => setShowAddEmployee(false)}>
                              Cancel
                            </Button>
                            <Button onClick={handleAddEmployee} disabled={isLoading}>
                              {isLoading ? "Adding..." : "Add Employee"}
                            </Button>
                          </DialogFooter>
                        </DialogContent>
                      </Dialog>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-2">
                      {employees.slice(0, 5).map((employee) => (
                        <div key={employee.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                          <div className="flex items-center space-x-3">
                            <Avatar className="h-10 w-10">
                              <AvatarImage src={employee.avatar || "/placeholder.svg"} alt={employee.name} />
                              <AvatarFallback>
                                {employee.name
                                  .split(" ")
                                  .map((n) => n[0])
                                  .join("")}
                              </AvatarFallback>
                            </Avatar>
                            <div>
                              <p className="text-sm font-medium text-gray-900">{employee.name}</p>
                              <p className="text-xs text-gray-500">
                                {employee.position} • {employee.department} • {formatCurrency(employee.salary)}
                              </p>
                            </div>
                          </div>
                          <Badge variant={employee.status === "active" ? "default" : "secondary"}>
                            {employee.status}
                          </Badge>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>

                {/* Payroll Integration */}
                <Card>
                  <CardHeader>
                    <CardTitle className="flex items-center">
                      <DollarSign className="mr-2 h-5 w-5 text-green-600" />
                      Payroll & Financial Integration
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                      <div className="bg-blue-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-blue-600 font-medium">Total Payroll</p>
                            <p className="text-xl font-bold text-blue-900">{formatCurrency(totalPayroll)}</p>
                          </div>
                          <DollarSign className="h-8 w-8 text-blue-600" />
                        </div>
                      </div>
                      <div className="bg-green-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-green-600 font-medium">Accounting Staff</p>
                            <p className="text-xl font-bold text-green-900">{accountingEmployees}</p>
                          </div>
                          <Calculator className="h-8 w-8 text-green-600" />
                        </div>
                      </div>
                      <div className="bg-purple-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-purple-600 font-medium">Avg Salary</p>
                            <p className="text-xl font-bold text-purple-900">
                              {formatCurrency(totalPayroll / totalEmployees)}
                            </p>
                          </div>
                          <BarChart3 className="h-8 w-8 text-purple-600" />
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>

              {/* HRMS Right Sidebar */}
              <div className="col-span-12 lg:col-span-4">
                <HRMSSidebar
                  currentTime={currentTime}
                  formatTime={formatTime}
                  formatDate={formatDate}
                  onSwitchToAccounting={() => handleDepartmentSwitch("accounting")}
                />
              </div>
            </div>
          </>
        ) : (
          // Accounting Dashboard
          <>
            {/* Accounting Quick Stats */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
              <StatCard
                title="Total Revenue"
                value={formatCurrency(financialData.revenue)}
                change="+12.5%"
                changeType="positive"
                icon={TrendingUp}
                color="green"
              />
              <StatCard
                title="Total Expenses"
                value={formatCurrency(financialData.expenses)}
                change="+8.2%"
                changeType="negative"
                icon={TrendingDown}
                color="red"
              />
              <StatCard
                title="Net Profit"
                value={formatCurrency(financialData.profit)}
                change="+18.7%"
                changeType="positive"
                icon={Target}
                color="blue"
              />
              <StatCard
                title="Cash Flow"
                value={formatCurrency(financialData.cashFlow)}
                change="+5.3%"
                changeType="positive"
                icon={Wallet}
                color="purple"
              />
            </div>

            <div className="grid grid-cols-12 gap-6">
              {/* Accounting Left Column */}
              <div className="col-span-12 lg:col-span-8">
                {/* Financial Overview */}
                <Card className="mb-6">
                  <CardHeader>
                    <CardTitle className="flex items-center">
                      <PieChart className="mr-2 h-5 w-5 text-green-600" />
                      Financial Overview
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div>
                        <h4 className="text-sm font-medium text-gray-900 mb-3">Revenue vs Expenses</h4>
                        <div className="space-y-3">
                          <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600">Revenue</span>
                            <span className="text-sm font-medium text-green-600">
                              {formatCurrency(financialData.revenue)}
                            </span>
                          </div>
                          <div className="w-full bg-gray-200 rounded-full h-2">
                            <div className="bg-green-500 h-2 rounded-full" style={{ width: "73%" }}></div>
                          </div>
                          <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600">Expenses</span>
                            <span className="text-sm font-medium text-red-600">
                              {formatCurrency(financialData.expenses)}
                            </span>
                          </div>
                          <div className="w-full bg-gray-200 rounded-full h-2">
                            <div className="bg-red-500 h-2 rounded-full" style={{ width: "54%" }}></div>
                          </div>
                        </div>
                      </div>
                      <div>
                        <h4 className="text-sm font-medium text-gray-900 mb-3">Key Metrics</h4>
                        <div className="space-y-3">
                          <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600">Profit Margin</span>
                            <span className="text-sm font-medium text-blue-600">26.5%</span>
                          </div>
                          <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600">ROI</span>
                            <span className="text-sm font-medium text-green-600">18.3%</span>
                          </div>
                          <div className="flex items-center justify-between">
                            <span className="text-sm text-gray-600">Cash Ratio</span>
                            <span className="text-sm font-medium text-purple-600">2.1</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Invoices & Bills */}
                <Card className="mb-6">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="flex items-center">
                        <Receipt className="mr-2 h-5 w-5 text-blue-600" />
                        Invoices & Bills
                      </CardTitle>
                      <Dialog open={showCreateInvoice} onOpenChange={setShowCreateInvoice}>
                        <DialogTrigger asChild>
                          <Button>
                            <Plus className="mr-2 h-4 w-4" />
                            Create Invoice
                          </Button>
                        </DialogTrigger>
                        <DialogContent>
                          <DialogHeader>
                            <DialogTitle>Create New Invoice</DialogTitle>
                          </DialogHeader>
                          <div className="space-y-4">
                            <div>
                              <Label htmlFor="clientName">Client Name *</Label>
                              <Input
                                id="clientName"
                                value={newInvoice.clientName}
                                onChange={(e) => setNewInvoice((prev) => ({ ...prev, clientName: e.target.value }))}
                                placeholder="Enter client name"
                              />
                            </div>
                            <div>
                              <Label htmlFor="amount">Amount *</Label>
                              <Input
                                id="amount"
                                type="number"
                                value={newInvoice.amount}
                                onChange={(e) => setNewInvoice((prev) => ({ ...prev, amount: e.target.value }))}
                                placeholder="Enter amount"
                              />
                            </div>
                            <div>
                              <Label htmlFor="dueDate">Due Date</Label>
                              <Input
                                id="dueDate"
                                type="date"
                                value={newInvoice.dueDate}
                                onChange={(e) => setNewInvoice((prev) => ({ ...prev, dueDate: e.target.value }))}
                              />
                            </div>
                            <div>
                              <Label htmlFor="description">Description</Label>
                              <Input
                                id="description"
                                value={newInvoice.description}
                                onChange={(e) => setNewInvoice((prev) => ({ ...prev, description: e.target.value }))}
                                placeholder="Enter description"
                              />
                            </div>
                          </div>
                          <DialogFooter>
                            <Button variant="outline" onClick={() => setShowCreateInvoice(false)}>
                              Cancel
                            </Button>
                            <Button onClick={handleCreateInvoice} disabled={isLoading}>
                              {isLoading ? "Creating..." : "Create Invoice"}
                            </Button>
                          </DialogFooter>
                        </DialogContent>
                      </Dialog>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                      <div className="bg-orange-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-orange-600 font-medium">Unpaid</p>
                            <p className="text-lg font-bold text-orange-900">{unpaidInvoicesCount}</p>
                            <p className="text-xs text-orange-700">{formatCurrency(financialData.unpaidInvoices)}</p>
                          </div>
                          <Clock className="h-6 w-6 text-orange-600" />
                        </div>
                      </div>
                      <div className="bg-red-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-red-600 font-medium">Overdue</p>
                            <p className="text-lg font-bold text-red-900">{overdueInvoicesCount}</p>
                            <p className="text-xs text-red-700">{formatCurrency(financialData.overdueInvoices)}</p>
                          </div>
                          <AlertTriangle className="h-6 w-6 text-red-600" />
                        </div>
                      </div>
                      <div className="bg-green-50 p-4 rounded-lg">
                        <div className="flex items-center justify-between">
                          <div>
                            <p className="text-sm text-green-600 font-medium">Paid</p>
                            <p className="text-lg font-bold text-green-900">
                              {invoices.filter((inv) => inv.status === "paid").length}
                            </p>
                            <p className="text-xs text-green-700">
                              {formatCurrency(
                                invoices
                                  .filter((inv) => inv.status === "paid")
                                  .reduce((sum, inv) => sum + inv.amount, 0),
                              )}
                            </p>
                          </div>
                          <CheckCircle className="h-6 w-6 text-green-600" />
                        </div>
                      </div>
                    </div>

                    <div className="space-y-2">
                      {invoices.slice(0, 5).map((invoice) => (
                        <div key={invoice.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                          <div>
                            <p className="text-sm font-medium text-gray-900">{invoice.invoiceNumber}</p>
                            <p className="text-xs text-gray-500">
                              {invoice.clientName} • Due: {invoice.dueDate}
                            </p>
                          </div>
                          <div className="flex items-center space-x-2">
                            <span className="text-sm font-medium">{formatCurrency(invoice.amount)}</span>
                            <Badge
                              variant={
                                invoice.status === "paid"
                                  ? "default"
                                  : invoice.status === "overdue"
                                    ? "destructive"
                                    : "secondary"
                              }
                            >
                              {invoice.status}
                            </Badge>
                          </div>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>

                {/* Payments */}
                <Card className="mb-6">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="flex items-center">
                        <CreditCard className="mr-2 h-5 w-5 text-purple-600" />
                        Payments
                      </CardTitle>
                      <Dialog open={showRecordPayment} onOpenChange={setShowRecordPayment}>
                        <DialogTrigger asChild>
                          <Button>
                            <Plus className="mr-2 h-4 w-4" />
                            Record Payment
                          </Button>
                        </DialogTrigger>
                        <DialogContent>
                          <DialogHeader>
                            <DialogTitle>Record New Payment</DialogTitle>
                          </DialogHeader>
                          <div className="space-y-4">
                            <div>
                              <Label htmlFor="paymentType">Payment Type *</Label>
                              <Select
                                value={newPayment.type}
                                onValueChange={(value: "incoming" | "outgoing") =>
                                  setNewPayment((prev) => ({ ...prev, type: value }))
                                }
                              >
                                <SelectTrigger>
                                  <SelectValue placeholder="Select payment type" />
                                </SelectTrigger>
                                <SelectContent>
                                  <SelectItem value="incoming">Incoming</SelectItem>
                                  <SelectItem value="outgoing">Outgoing</SelectItem>
                                </SelectContent>
                              </Select>
                            </div>
                            <div>
                              <Label htmlFor="paymentAmount">Amount *</Label>
                              <Input
                                id="paymentAmount"
                                type="number"
                                value={newPayment.amount}
                                onChange={(e) => setNewPayment((prev) => ({ ...prev, amount: e.target.value }))}
                                placeholder="Enter amount"
                              />
                            </div>
                            <div>
                              <Label htmlFor="paymentMethod">Payment Method *</Label>
                              <Select
                                value={newPayment.method}
                                onValueChange={(value: "cash" | "bank" | "card" | "cheque") =>
                                  setNewPayment((prev) => ({ ...prev, method: value }))
                                }
                              >
                                <SelectTrigger>
                                  <SelectValue placeholder="Select payment method" />
                                </SelectTrigger>
                                <SelectContent>
                                  <SelectItem value="cash">Cash</SelectItem>
                                  <SelectItem value="bank">Bank Transfer</SelectItem>
                                  <SelectItem value="card">Card</SelectItem>
                                  <SelectItem value="cheque">Cheque</SelectItem>
                                </SelectContent>
                              </Select>
                            </div>
                            <div>
                              <Label htmlFor="paymentDescription">Description *</Label>
                              <Input
                                id="paymentDescription"
                                value={newPayment.description}
                                onChange={(e) => setNewPayment((prev) => ({ ...prev, description: e.target.value }))}
                                placeholder="Enter description"
                              />
                            </div>
                          </div>
                          <DialogFooter>
                            <Button variant="outline" onClick={() => setShowRecordPayment(false)}>
                              Cancel
                            </Button>
                            <Button onClick={handleRecordPayment} disabled={isLoading}>
                              {isLoading ? "Recording..." : "Record Payment"}
                            </Button>
                          </DialogFooter>
                        </DialogContent>
                      </Dialog>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-2">
                      {payments.slice(0, 5).map((payment) => (
                        <div key={payment.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                          <div className="flex items-center space-x-3">
                            <div
                              className={`p-2 rounded-full ${payment.type === "incoming" ? "bg-green-100" : "bg-red-100"}`}
                            >
                              {payment.type === "incoming" ? (
                                <TrendingUp className="h-4 w-4 text-green-600" />
                              ) : (
                                <TrendingDown className="h-4 w-4 text-red-600" />
                              )}
                            </div>
                            <div>
                              <p className="text-sm font-medium text-gray-900">{payment.description}</p>
                              <p className="text-xs text-gray-500">
                                {payment.method} • {payment.date}
                              </p>
                            </div>
                          </div>
                          <div className="flex items-center space-x-2">
                            <span
                              className={`text-sm font-medium ${payment.type === "incoming" ? "text-green-600" : "text-red-600"}`}
                            >
                              {payment.type === "incoming" ? "+" : "-"}
                              {formatCurrency(payment.amount)}
                            </span>
                            <Badge variant={payment.status === "completed" ? "default" : "secondary"}>
                              {payment.status}
                            </Badge>
                          </div>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>

                {/* Journal Entries */}
                <Card>
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="flex items-center">
                        <FileText className="mr-2 h-5 w-5 text-indigo-600" />
                        Journal Entries
                      </CardTitle>
                      <Dialog open={showJournalEntry} onOpenChange={setShowJournalEntry}>
                        <DialogTrigger asChild>
                          <Button>
                            <Plus className="mr-2 h-4 w-4" />
                            Add Entry
                          </Button>
                        </DialogTrigger>
                        <DialogContent>
                          <DialogHeader>
                            <DialogTitle>Add Journal Entry</DialogTitle>
                          </DialogHeader>
                          <div className="space-y-4">
                            <div>
                              <Label htmlFor="journalType">Entry Type *</Label>
                              <Select
                                value={newJournal.type}
                                onValueChange={(value: "sales" | "purchase" | "cash" | "bank") =>
                                  setNewJournal((prev) => ({ ...prev, type: value }))
                                }
                              >
                                <SelectTrigger>
                                  <SelectValue placeholder="Select entry type" />
                                </SelectTrigger>
                                <SelectContent>
                                  <SelectItem value="sales">Sales</SelectItem>
                                  <SelectItem value="purchase">Purchase</SelectItem>
                                  <SelectItem value="cash">Cash</SelectItem>
                                  <SelectItem value="bank">Bank</SelectItem>
                                </SelectContent>
                              </Select>
                            </div>
                            <div>
                              <Label htmlFor="journalDescription">Description *</Label>
                              <Input
                                id="journalDescription"
                                value={newJournal.description}
                                onChange={(e) => setNewJournal((prev) => ({ ...prev, description: e.target.value }))}
                                placeholder="Enter description"
                              />
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                              <div>
                                <Label htmlFor="debit">Debit Amount</Label>
                                <Input
                                  id="debit"
                                  type="number"
                                  value={newJournal.debit}
                                  onChange={(e) => setNewJournal((prev) => ({ ...prev, debit: e.target.value }))}
                                  placeholder="0.00"
                                />
                              </div>
                              <div>
                                <Label htmlFor="credit">Credit Amount</Label>
                                <Input
                                  id="credit"
                                  type="number"
                                  value={newJournal.credit}
                                  onChange={(e) => setNewJournal((prev) => ({ ...prev, credit: e.target.value }))}
                                  placeholder="0.00"
                                />
                              </div>
                            </div>
                            <div>
                              <Label htmlFor="reference">Reference</Label>
                              <Input
                                id="reference"
                                value={newJournal.reference}
                                onChange={(e) => setNewJournal((prev) => ({ ...prev, reference: e.target.value }))}
                                placeholder="Enter reference"
                              />
                            </div>
                          </div>
                          <DialogFooter>
                            <Button variant="outline" onClick={() => setShowJournalEntry(false)}>
                              Cancel
                            </Button>
                            <Button onClick={handleAddJournalEntry} disabled={isLoading}>
                              {isLoading ? "Adding..." : "Add Entry"}
                            </Button>
                          </DialogFooter>
                        </DialogContent>
                      </Dialog>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-2">
                      {journalEntries.slice(0, 5).map((entry) => (
                        <div key={entry.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                          <div>
                            <p className="text-sm font-medium text-gray-900">{entry.description}</p>
                            <p className="text-xs text-gray-500">
                              {entry.type} • {entry.date} • {entry.reference}
                            </p>
                          </div>
                          <div className="flex items-center space-x-4">
                            {entry.debit > 0 && (
                              <span className="text-sm text-green-600">Dr: {formatCurrency(entry.debit)}</span>
                            )}
                            {entry.credit > 0 && (
                              <span className="text-sm text-red-600">Cr: {formatCurrency(entry.credit)}</span>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              </div>

              {/* Accounting Right Sidebar */}
              <div className="col-span-12 lg:col-span-4">
                <AccountingSidebar
                  currentTime={currentTime}
                  formatTime={formatTime}
                  formatDate={formatDate}
                  formatCurrency={formatCurrency}
                  bankAccounts={bankAccounts}
                  financialData={financialData}
                  onSwitchToHRMS={() => handleDepartmentSwitch("hrms")}
                />
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

// HRMS Sidebar Component
// Bhai, yahan pe types add karne hain taake TypeScript ka error na aaye
type HRMSSidebarProps = {
  currentTime: Date;
  formatTime: (date: Date) => string;
  formatDate: (date: Date) => string;
  onSwitchToAccounting: () => void;
};

function HRMSSidebar({ currentTime, formatTime, formatDate, onSwitchToAccounting }: HRMSSidebarProps) {
  return (
    <>
      {/* System Time */}
      <Card className="mb-6">
        <CardContent className="p-4">
          <div className="text-center">
            <div className="text-sm text-gray-500 mb-1">Current Time</div>
            <div className="text-2xl font-bold text-gray-900 mb-1">{formatTime(currentTime)}</div>
            <div className="text-sm text-gray-600">{formatDate(currentTime)}</div>
          </div>
        </CardContent>
      </Card>

      {/* Quick Actions */}
      <Card className="mb-6">
        <CardHeader>
          <CardTitle className="text-base">Quick Actions</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-3">
            <QuickActionButton icon={UserPlus} label="Add Employee" onClick={() => {}} />
            <QuickActionButton icon={DollarSign} label="Payroll" onClick={() => {}} />
            <QuickActionButton icon={Calculator} label="Accounting" onClick={onSwitchToAccounting} />
            <QuickActionButton icon={FileSpreadsheet} label="Reports" onClick={() => {}} />
          </div>
        </CardContent>
      </Card>

      {/* HR-Finance Integration */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">HR-Finance Integration</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="flex items-center justify-between p-2 bg-blue-50 rounded-lg">
              <span className="text-sm text-blue-700">Payroll Sync</span>
              <Badge className="bg-blue-100 text-blue-800">Active</Badge>
            </div>
            <div className="flex items-center justify-between p-2 bg-green-50 rounded-lg">
              <span className="text-sm text-green-700">Expense Tracking</span>
              <Badge className="bg-green-100 text-green-800">Live</Badge>
            </div>
            <div className="flex items-center justify-between p-2 bg-purple-50 rounded-lg">
              <span className="text-sm text-purple-700">Budget Allocation</span>
              <Badge className="bg-purple-100 text-purple-800">Updated</Badge>
            </div>
          </div>
        </CardContent>
      </Card>
    </>
  )
}

// Accounting Sidebar Component
function AccountingSidebar({
  currentTime,
  formatTime,
  formatDate,
  formatCurrency,
  bankAccounts,
  financialData,
  onSwitchToHRMS,
}: {
  currentTime: Date
  formatTime: (date: Date) => string
  formatDate: (date: Date) => string
  formatCurrency: (amount: number) => string
  bankAccounts: BankAccount[]
  financialData: any
  onSwitchToHRMS: () => void
}) {
  return (
    <>
      {/* System Time */}
      <Card className="mb-6">
        <CardContent className="p-4">
          <div className="text-center">
            <div className="text-sm text-gray-500 mb-1">Current Time</div>
            <div className="text-2xl font-bold text-gray-900 mb-1">{formatTime(currentTime)}</div>
            <div className="text-sm text-gray-600">{formatDate(currentTime)}</div>
          </div>
        </CardContent>
      </Card>

      {/* Quick Actions */}
      <Card className="mb-6">
        <CardHeader>
          <CardTitle className="text-base">Quick Actions</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-3">
            <QuickActionButton icon={Receipt} label="New Invoice" onClick={() => {}} />
            <QuickActionButton icon={CreditCard} label="Record Payment" onClick={() => {}} />
            <QuickActionButton icon={FileText} label="Journal Entry" onClick={() => {}} />
            <QuickActionButton icon={Download} label="Export Report" onClick={() => {}} />
            <QuickActionButton icon={Users} label="HR System" onClick={onSwitchToHRMS} />
            <QuickActionButton icon={Settings} label="Settings" onClick={() => {}} />
          </div>
        </CardContent>
      </Card>

      {/* Bank Accounts */}
      <Card className="mb-6">
        <CardHeader>
          <CardTitle className="text-base">Bank Accounts</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {bankAccounts.map((account: any) => (
              <div key={account.id} className="p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center justify-between mb-1">
                  <span className="text-sm font-medium text-gray-900">{account.name}</span>
                  <span className="text-sm font-bold text-green-600">{formatCurrency(account.balance)}</span>
                </div>
                <div className="flex items-center justify-between text-xs text-gray-500">
                  <span>Last reconciled: {account.lastReconciled}</span>
                  {account.unmatchedTransactions > 0 && (
                    <Badge variant="outline" className="text-orange-600 border-orange-300">
                      {account.unmatchedTransactions} unmatched
                    </Badge>
                  )}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Financial Alerts */}
      <Card className="mb-6">
        <CardHeader>
          <CardTitle className="text-base">Financial Alerts</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="flex items-start space-x-2 p-2 bg-orange-50 rounded-lg">
              <AlertTriangle className="h-4 w-4 text-orange-600 mt-0.5" />
              <div>
                <p className="text-xs font-medium text-orange-800">Overdue Invoices</p>
                <p className="text-xs text-orange-600">{formatCurrency(financialData.overdueInvoices)} pending</p>
              </div>
            </div>
            <div className="flex items-start space-x-2 p-2 bg-blue-50 rounded-lg">
              <Clock className="h-4 w-4 text-blue-600 mt-0.5" />
              <div>
                <p className="text-xs font-medium text-blue-800">Tax Deadline</p>
                <p className="text-xs text-blue-600">Due in 15 days</p>
              </div>
            </div>
            <div className="flex items-start space-x-2 p-2 bg-green-50 rounded-lg">
              <CheckCircle className="h-4 w-4 text-green-600 mt-0.5" />
              <div>
                <p className="text-xs font-medium text-green-800">Cash Flow</p>
                <p className="text-xs text-green-600">Positive trend</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* HR-Finance Integration */}
      <Card>
        <CardHeader>
          <CardTitle className="text-base">HR-Finance Integration</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="flex items-center justify-between p-2 bg-blue-50 rounded-lg">
              <span className="text-sm text-blue-700">Employee Expenses</span>
              <Badge className="bg-blue-100 text-blue-800">Synced</Badge>
            </div>
            <div className="flex items-center justify-between p-2 bg-green-50 rounded-lg">
              <span className="text-sm text-green-700">Payroll Integration</span>
              <Badge className="bg-green-100 text-green-800">Active</Badge>
            </div>
            <div className="flex items-center justify-between p-2 bg-purple-50 rounded-lg">
              <span className="text-sm text-purple-700">Department Budgets</span>
              <Badge className="bg-purple-100 text-purple-800">Updated</Badge>
            </div>
          </div>
        </CardContent>
      </Card>
    </>
  )
}

// StatCard component ka type define karte hain taake TypeScript errors na aayein
type StatCardProps = {
  title: string
  value: string | number
  change: string | number
  changeType: "positive" | "negative" | "neutral"
  icon: React.ElementType
  color: "blue" | "green" | "orange" | "purple" | "red"
}

// Component for stat cards
function StatCard({ title, value, change, changeType, icon: Icon, color }: StatCardProps) {
  const colorClasses = {
    blue: "bg-blue-50 text-blue-600 border-blue-200",
    green: "bg-green-50 text-green-600 border-green-200",
    orange: "bg-orange-50 text-orange-600 border-orange-200",
    purple: "bg-purple-50 text-purple-600 border-purple-200",
    red: "bg-red-50 text-red-600 border-red-200",
  }

  return (
    <Card>
      <CardContent className="p-6">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium text-gray-600">{title}</p>
            <p className="text-2xl font-bold text-gray-900">{value}</p>
            <p
              className={`text-sm ${changeType === "positive" ? "text-green-600" : changeType === "negative" ? "text-red-600" : "text-gray-600"}`}
            >
              {change} from last month
            </p>
          </div>
          <div className={`p-3 rounded-full ${colorClasses[color as keyof typeof colorClasses]}`}>
            <Icon className="h-6 w-6" />
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

// QuickActionButton component ka type define karte hain taake TypeScript errors na aayein
type QuickActionButtonProps = {
  icon: React.ElementType
  label: string
  onClick: () => void
}

// Component for quick action buttons
function QuickActionButton({ icon: Icon, label, onClick }: QuickActionButtonProps) {
  return (
    <Button
      variant="outline"
      className="h-auto py-3 flex flex-col items-center space-y-1 bg-transparent"
      onClick={onClick}
    >
      <Icon className="h-5 w-5 text-blue-600" />
      <span className="text-xs">{label}</span>
    </Button>
  )
}
