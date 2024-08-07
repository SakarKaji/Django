from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from .forms import StudentRegistration
from .models import User
# Create your views here.

# this function adds new item and shows item
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save() 
            fm = StudentRegistration() 
    else:
        fm = StudentRegistration() 
    stud = User.objects.all
    
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})

# this function will update/edit
def update_data(request, id): #if the id is clicked 1 then pk=1
    if request.method == 'POST':
        dl = User.objects.get(pk=id)  #pk = primary key
        fm = StudentRegistration(request.POST, instance=dl)
        if fm.is_valid(): 
            fm.save()

    else: #if the edit button is not click then GET
        dl = User.objects.get(pk=id)  #pk = primary key
        fm = StudentRegistration(instance=dl)

    return render(request, 'enroll/updatestudent.html', {'form':fm})

# this function is used to delete the data
def delete_data(request, id): #(request, id): dynamic url because to work on specific data , #if the id is clicked 1 then pk=1 
    if request.method == 'POST': #we can also do this by GET but we are doing this by POST
        dl = User.objects.get(pk=id)  #pk = primary key
        dl.delete()
        return HttpResponseRedirect('/') #this will redirect to the homepage


# # this function will update/edit
# def update_data(request, id): #if the id is clicked 1 then pk=1
#     if request.method == 'POST':
#         dl = User.objects.get(pk=id)  #pk = primary key
#         fm = StudentRegistration(request.POST, instance=dl)
#         if fm.is_valid(): 
#             fm.save()

#     else: #if the edit button is not click then GET
#         dl = User.objects.get(pk=id)  #pk = primary key
#         fm = StudentRegistration(instance=dl)

#     return render(request, 'enroll/updatestudent.html', {'form':fm})

    



    