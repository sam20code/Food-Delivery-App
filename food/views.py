from food.form import ItemForm
from .models import Item
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def userHomePage(request):
    itm_list = Item.objects.all()
    context ={
        'item_list' : itm_list,
    }
    return render(request,'food/userHomePage.html',context)
    
def credentials(request):
    return render(request,'food/Credentials.html')

def adminHomePage(request):
    itm_list = Item.objects.filter(item_userRole=request.user.username)
    context ={
        'item_list' : itm_list,
    }
    return render(request,'food/adminHomePage.html',context)
    
def credentials(request):
    return render(request,'food/Credentials.html')

#user signup and login
def userSignUp(request):
    if request.method == 'POST':
        username=request.POST['userName']
        email=request.POST['userEmail']
        password=request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('food:credentials')
    
def userlogIn(request):
    if request.method == 'POST':
        username=request.POST['userName']
        password=request.POST['userPassword']

        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect('food:userHomePage')
        
#admin sign up and login  
def adminSignUp(request):
    if request.method == 'POST':
        username=request.POST['newAdminName']
        email=request.POST['newAdminEmail']
        password=request.POST['newAdminPassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('food:credentials')
    
def adminlogIn(request):
    if request.method == 'POST':
        username=request.POST['adminName']
        password=request.POST['adminPassword']

        myuser = authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            return redirect('food:adminHomePage')
        


def userDetails(request,item_id:int):
    item = Item.objects.get(pk = item_id)
    context = {
        'item':item,
    }
    return render(request,'food/userDetails.html',context)

def adminDetails(request,item_id:int):
    item = Item.objects.get(pk = item_id)
    context = {
        'item':item,
    }
    return render(request,'food/adminDetails.html',context)

def addItems(request):
    form  = ItemForm(request.POST,request.FILES)
    if form.is_valid(): 
        form.save()
        return redirect('food:adminHomePage')
    return render(request,'food/AddItems.html',{'form':form})

def editItem(request,item_id):
    item = Item.objects.get(pk = item_id)
    form  = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        # form.cleaned_data['item_userRole']=request.user.username
        form.save()
        return redirect('food:adminHomePage')
    return render(request,'food/AddItems.html',{'form':form,'item':item})

def deleteItem(request,item_id):
    item = Item.objects.get(pk = item_id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/deleteItem.html',{'item':item})
