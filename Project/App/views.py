from django.shortcuts import render, redirect
from .models import Department, Employee

# Create your views here.
def Validations(data):
    pass


def home(request):
    empList = Employee.objects.all()
    return render(request, 'home.html', { 'empList' : empList })

def create(request):
    if request.method == "GET":
        deptList = Department.objects.all()
        return render(request, 'create.html', { 'deptList' : deptList })
    else:
        if request.POST.get("action") == "Register":
            # try:                
                #Insert the data into the database table : By using model class object
                Validations(request.POST)

                dept = Department.objects.get(DeptNo = (request.POST.get('DeptNo')))            
                Employee.objects.create(
                    EmpId = request.POST.get('EmpId'),
                    Ename = request.POST.get('Ename'),
                    Password = request.POST.get('Password'),
                    Gender = request.POST.get('Gender'),
                    Dob = request.POST.get('Dob'),
                    Phone = request.POST.get('Phone'),
                    Email = request.POST.get('Email'),
                    Salary = request.POST.get('Salary'),
                    Address = request.POST.get('Address'),
                    DeptNo = dept
                )
            # except Exception:
            #     return HttpResponse("Something wrong happend...!")
            
        return redirect('home')

def edit(request, EmpId):
    return render(request, 'edit.html')

def delete(request, EmpId):
   return render(request, 'delete.html')

def pagenotfound(request):
    return render(request, 'pagenotfound.html')

# def httpExceptionHandle(request, exception):
#     return render(request, <Create one Html>, {'exception' : exception})