from django.shortcuts import render, redirect
from django.db import models
from django.views.generic.list import ListView
from django_tables2 import RequestConfig
from . import models
from main.tables import studentsTable, adminsTable, dormsTable, roomsTable, majorsTable, deptTable
from . import forms
from django.contrib.auth import logout

# Create your views here.
#class listofstudents(ListView):
#    model = students
#
#def students(request):
#    data = models.students.objects.all()
#    
#    return render(request, 'sth.html', {'students' : data})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'home.html')


def students(request):
    table = studentsTable(models.students.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'students.html', {'table': table})


def admins(request):
    if request.user.is_authenticated:
        table = adminsTable(models.admins.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'admins.html', {'table': table})
    else:
        return render(request, 'admininsertion.html')

def dept(request):
    if request.user.is_authenticated:
        table = deptTable(models.dept.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'dept.html', {'table': table})
    else:
        return render(request, 'admininsertion.html')

def dorms(request):
    if request.user.is_authenticated:
        table = dormsTable(models.dorms.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'dorms.html', {'table': table})
    else:
        return render(request, 'admininsertion.html')

def rooms(request):
    if request.user.is_authenticated:
        table = roomsTable(models.rooms.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'rooms.html', {'table': table})
    else:
        return render(request, 'admininsertion.html')

def majors(request):
    if request.user.is_authenticated:
        table = majorsTable(models.majors.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'majors.html', {'table': table})
    else:
        return render(request, 'admininsertion.html')

def insert_students(request):
    if request.user.is_authenticated:
        form = forms.studentinsertion()
        if request.method == 'POST':
            form = forms.studentinsertion(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')
        return render(request, 'studentinsertion.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')

def success(request):
    return render(request, 'success.html')


def insert_admins(request):
    if request.user.is_authenticated:
        form = forms.admininsertion()
        if request.method == 'POST':
            form = forms.admininsertion(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')
        return render(request, 'admininsertion.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')
    

def insert_dorms(request):
    if request.user.is_authenticated:
        form = forms.dorminsertion()
        if request.method == 'POST':
            form = forms.dorminsertion(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')
        return render(request, 'dorminsertion.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')

def insert_rooms(request):
    if request.user.is_authenticated:
        form = forms.roominsertion()
        if request.method == 'POST':
            form = forms.roominsertion(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')
        return render(request, 'roominsertion.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')


def insert_majors(request):
    if request.user.is_authenticated:
        form = forms.majorinsertion()
        if request.method == 'POST':
            form = forms.majorinsertion(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')
        return render(request, 'majorinsertion.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')
    
    
def addadmin(request):
    if request.user.is_authenticated:
        form = forms.addadmin()
        if request.method == 'POST':
            form = forms.addadmin(request.POST)
            if form.is_valid():
                #print(form)
                objec = models.admins.objects.get(roll = form.cleaned_data['roll'])
                objec.delete()
                objec = models.admins(name=form.cleaned_data['name'],major=form.cleaned_data['major'], dept=form.cleaned_data['dept'], roll=form.cleaned_data['roll'])
                objec.save()
                return render(request, 'success.html')
        return render(request, 'addadmin.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')



def updatestudent(request):
    if request.user.is_authenticated:
        form = forms.updatestudent()
        if request.method == 'POST':
            form = forms.updatestudent(request.POST)
            if form.is_valid():
                #print(form)
                objec = models.students.objects.get(student_id = form.cleaned_data['student_id'])
                objec.delete()
                objec = models.admins(student_id=form.cleaned_data['student_id'],first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], major=form.cleaned_data['major'], type_degree=form.cleaned_data['type_degree'])
                objec.save()
                return render(request, 'success.html')
        return render(request, 'updatestudent.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')
    
    

def updateroom(request):
    if request.user.is_authenticated:
        form = forms.updateroom()
        if request.method == 'POST':
            form = forms.updateroom(request.POST)
            if form.is_valid():
                #print(form)
                objec = models.rooms.objects.get(room_id = form.cleaned_data['room_id'])
                objec.delete()
                objec = models.admins(room_id=form.cleaned_data['room_id'],room_statue=form.cleaned_data['room_statue'], room_admin=form.cleaned_data['room_admin'])
                objec.save()
                return render(request, 'success.html')
        return render(request, 'updateroom.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')
    
    
    
    
def updateroom(request):
    if request.user.is_authenticated:
        form = forms.updateroom()
        if request.method == 'POST':
            form = forms.updateroom(request.POST)
            if form.is_valid():
                #print(form)
                objec = models.rooms.objects.get(room_id = form.cleaned_data['room_id'])
                objec.delete()
                objec = models.admins(room_id=form.cleaned_data['room_id'],room_statue=form.cleaned_data['room_statue'], room_admin=form.cleaned_data['room_admin'])
                objec.save()
                return render(request, 'success.html')
        return render(request, 'updateroom.html', {'form' : form})
    else:
        return render(request, 'admininsertion.html')
    
