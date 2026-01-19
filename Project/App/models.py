from django.db import models

# Create your models here.
class Department(models.Model):
    DeptNo = models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Dname} ({self.DeptNo})"
    
    class Meta:
        db_table = 'department'

class Employee(models.Model):
    EmpId = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Gender = models.CharField(max_length=6)
    Dob = models.DateField()
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Salary = models.FloatField()
    Address = models.CharField(max_length=200)
    DeptNo = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='DeptNo')

    def __str__(self):
        return f"{self.EmpId} ({self.Ename})"
    
    class Meta:
        db_table = 'employee'        