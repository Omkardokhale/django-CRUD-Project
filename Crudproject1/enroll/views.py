from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User



# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistration(request.POST)

     if fm.is_valid():
        
        nm = fm.cleaned_data['Name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']
        reg = User(Name=nm, email=em, password=pw)
        reg.save()
        fm = StudentRegistration()
        stud = User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})
    else:
        fm = StudentRegistration()
        stud = User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})



# This Function update and edit
def update_data(request, id):
    if request.method== 'POST':
      pi=User.objects.get(pk=id)
      fm = StudentRegistration(request.POST, instance=pi)

      if fm.is_valid():
        fm.save()

    else:
         pi = User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)   

         return render(request, 'enroll/updatestudent.html', {'form': fm})



        # This function are delete.


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
