from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import Add_room 
from .forms import Book_Room_User
from .forms import RegisterForm
from .import models
from .models import Profile

def Add_Room(request):
    return render(request,'HMS/Add_Room.html',
    {
        'FORM': Add_room()
    })


def User_Profile(request):
    return render(request,'HMS/Profile.html')

def Book_Room(request):
    return render(request,'HMS/Book_Room.html',
    {
        'FORM': Book_Room_User()
    })

def Cancel_Booking(request):
    return render(request,'HMS/Cancel_Booking.html')

def Customer_HomePage(request):
    return render(request,'HMS/Customer_HomePage.html')


def About_us(request):
    return render(request,'HMS/About_us.html')

def Contact_us(request):
    return render(request,'HMS/Contact_us.html')

def Booking_History(request):
    return render(request,'HMS/Booking_History.html')

def Payment_Method(request):
    return render(request,'HMS/Payment_Method.html')

def Manager_Report(request):
    return render(request,'HMS/View_Report.html')

def Manager_Profile(request):
    return render(request,'HMS/Manager_Profile.html')

def Manager_Bookings(request):
    return render(request,'HMS/View_Bookings.html')

def Manager_login(request):
    return render(request,'HMS/Manager-login.html')

def Request_Form(request):
    return render(request,'HMS/Request_Form.html')

def Feedback_Form(request):
    return render(request,'HMS/Feedback_form.html')



def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.save()
			user.refresh_from_db()
			user.profile.First_Name = form.cleaned_data.get('First_Name')
			user.profile.Last_Name = form.cleaned_data.get('Last_Name')
			user.profile.CNIC = form.cleaned_data.get('CNIC')
			user.profile.Contact_Number = form.cleaned_data.get('Contact_Number')
			user.profile.Email = form.cleaned_data.get('Email')
			user.save()
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password1)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("Customer")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	else:
		form = RegisterForm()
	return render (request=request, template_name="HMS/register.html", context={"register_form":form})






def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("Customer")
			else:
				form = AuthenticationForm()
				messages.error(request,"Invalid username or password.")
				return render(request=request, template_name="HMS/login.html", context={"login_form":form})
		else:
			form = AuthenticationForm()
			messages.error(request,"Invalid username or password.")
			return render(request=request, template_name="HMS/login.html", context={"login_form":form})
	form = AuthenticationForm()
	return render(request=request, template_name="HMS/login.html", context={"login_form":form})
