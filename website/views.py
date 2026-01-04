from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()

    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        #Authenticate
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have logged in")
            return redirect('home')
        else:
            messages.success(request, "There is an error")
            return redirect('home')
    else:
        return render(request, 'home.html', {'record':records})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "you have registered sucessfully")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form })
    return render(request, 'register.html', {'form':form })

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return render(request, 'home.html')

def record(request, id):
    if request.user.is_authenticated:
        # looking in the record for id
        record = Record.objects.get(id=id)
        return render(request, 'record.html',{'record':record})
    else:
        return redirect('home')
def delete_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
    
def add_record(request):

    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, "Record is saved")
            return redirect('home')
        return render(request, 'addrecord.html', {'form':form})
    else:
        messages.success(request, "you may be logged in")
        return redirect('home')

def update_record(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'updaterecord.html', {'form':form})
    else:
        messages.success(request, "You may be logged in")
        return redirect('home')
