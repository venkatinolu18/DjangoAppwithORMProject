from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('edit/<int:EmpId>/', views.edit, name="edit"), #Query parameter
    path('delete/<int:EmpId>/', views.delete, name="delete"),
    path('<path:pagename>/', views.pagenotfound, name="pagenotfound")
]