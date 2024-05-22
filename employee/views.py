from django.views.generic import CreateView, DeleteView,DetailView,ListView,UpdateView
from .models import Employee
from django.urls import reverse_lazy
# Create your views here.
class EmployeeCreate(CreateView):
    model = Employee
    fields=['first_name','last_name',
            "phone_number","age","is_married",
            "children","is_dicorced","salary",
            "hired_at","passport_id","is_handicapped",
            "role","current_health","illness",
            "family_health","underages"]
    
    success_url = reverse_lazy('employee')  # return to the list view by default
    
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy("employees")

class EmployeeDetail(DetailView):
    model = Employee

def pointCalc(model):
    gx=0
    mp=0

class EmployeeList(ListView):
    model = Employee



class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy("employee")


