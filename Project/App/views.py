from django.shortcuts import render, redirect
from .models import Department, Employee
from re import match

# Create your views here.
def Validations(data):
    errors = {}
    
    if not data.get('EmpId'):
        errors['EmpId'] = "*Employee Id is required."
    elif not data.get('EmpId').isdigit():
        errors['EmpId'] = "*Employee Id must be numeric."

    if not data.get('Ename'):
        errors['Ename'] = "*Employee Name is required."
    elif any(char.isdigit() for char in data.get('Ename')):
        errors['Ename'] = "*Employee Name should not contain numbers."

    if not data.get('Password'):
        errors['Password'] = "*Password is required."

    if not data.get('Gender'):
        errors['Gender'] = "*Gender is required."

    if not data.get('Dob'): 
        errors['Dob'] = "*Date of Birth is required."  

    if not data.get('Phone'):
        errors['Phone'] = "*Phone number is required." 
    elif not data.get('Phone').isdigit():
        errors['Phone'] = "*Phone number must be numeric."
    elif len(data.get('Phone')) != 10:
        errors['Phone'] = "*Phone number must be 10 digits long."

    if not data.get('Email'):
        errors['Email'] = "*Email address is required."  
    elif match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data.get('Email')) is None:
        errors['Email'] = "*Invalid email address."

    if not data.get('Salary'):
        errors['Salary'] = "*Salary is required."

    if not data.get('Address'):
        errors['Address'] = "*Address is required."

    if not data.get('DeptNo') or data.get('DeptNo') == '0':
        errors['DeptNo'] = "*Department selection is required."

    return errors


def home(request):
    empList = Employee.objects.all()
    return render(request, 'home.html', { 'empList' : empList })

def create(request):
    if request.method == "GET":
        deptList = Department.objects.all()
        return render(request, 'create.html', { 'deptList' : deptList })
    else:
        if request.POST.get("action") == "Register":
            try:                
                #Insert the data into the database table : By using model class object
                errors = Validations(request.POST)
                if errors:
                    deptList = Department.objects.all()
                    return render(request, 'create.html', { 'deptList' : deptList, 'errors': errors, 'data': request.POST })

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
            except Exception:
                return redirect("exception", exception= Exception("Error occurred while inserting record into Employee table."))

        return redirect('home')

def edit(request, EmpId):
    if request.method == "GET":
        deptList = Department.objects.all()
        emp = Employee.objects.get(EmpId=EmpId)
        return render(request, 'edit.html', { 'emp' : emp, 'deptList' : deptList })
    else:
        if request.POST.get("action") == "Update":
            Validations(request.POST)

            dept = Department.objects.get(DeptNo = (request.POST.get('DeptNo')))
            emp = Employee.objects.get(EmpId=EmpId)
            emp.Ename = request.POST.get('Ename')
            emp.Password = request.POST.get('Password')
            emp.Gender = request.POST.get('Gender')
            emp.Dob = request.POST.get('Dob')
            emp.Phone = request.POST.get('Phone')
            emp.Email = request.POST.get('Email')
            emp.Salary = request.POST.get('Salary')
            emp.Address = request.POST.get('Address')
            emp.DeptNo = dept
            emp.save() # Update the record in the database table

        return redirect('home')

    

def delete(request, EmpId):
    if request.method == "POST":
        if request.POST.get("action") == "Do you really want to delete this record?":
            emp = Employee.objects.get(EmpId=EmpId)
            emp.delete() # Delete the record from the database table

        return redirect('home')
    else:
        deptList = Department.objects.all()
        emp = Employee.objects.get(EmpId=EmpId)
        return render(request, 'delete.html', { 'emp' : emp , 'deptList' : deptList })



def pagenotfound(request, exception):
    return render(request, 'pagenotfound.html', status=404)

def httpExceptionHandle(request):
    return render(request, 'exception.html', status=500)