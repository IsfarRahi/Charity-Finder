from django.shortcuts import render,redirect
from charity.forms import CharityForm
from charity.models import Charity
# Create your views here.

def make(request):
    if request.POST:
        form = CharityForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/all-list")
    else:
        form = CharityForm()


    return render(request,'make.html',{'form':form})

def show(request):
    charities = Charity.objects.all()
    return render(request,"show.html",{'charities':charities})

def delete(request,id):
    charity=Charity.objects.get(id=id)
    charity.delete()
    return redirect("/all-list")

def edit(request,id):
    charity=Charity.objects.get(id=id)
    return render(request,'edit.html',{'charity':charity})

def update(request,id):
    charity = Charity.objects.get(id=id)
    form = CharityForm(request.POST,instance=charity)


    if form.is_valid():
       charity.save()
       return redirect("/all-list")


       return render(request, 'edit.html', {'charity': charity})