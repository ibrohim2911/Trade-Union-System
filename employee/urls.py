from django.urls import path
from .views import EmployeeList,EmployeeDelete,EmployeeDetail,EmployeeCreate,EmployeeUpdate
urlpatterns = [
    path('employees/', EmployeeList.as_view(), name="employees"),
    path('employee/delete', EmployeeDelete.as_view(), name="employeeDelete"),
    path('employee/', EmployeeDetail.as_view(), name="employee"),
    path('employee/new', EmployeeCreate.as_view(), name="employeeCreate"),
    path('employee/edit', EmployeeUpdate.as_view(), name="employeeUpdate"),
]