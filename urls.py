from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Profile/',views.User_Profile,name="Profile"),
    path('login/',views.login_request,name="login"),
    path("register/", views.register_request, name="register"),
    path("Customer/", views.Customer_HomePage, name="Customer"),
    path("About/", views.About_us, name="About"),
    path("Contact_us/", views.Contact_us, name="Contact_us"),
    path("Book_Room/", views.Book_Room, name="Book_Room"),
    path("Cancel_Booking/", views.Cancel_Booking, name="Cancel_Booking"),
    path("Add_Room/", views.Add_Room, name="Add_Room"),
    path("Booking_History/", views.Booking_History, name="Booking_History"),
    path("Payment_Method/", views.Payment_Method, name="Payment_Method"),
    path("Manager_Report/", views.Manager_Report, name="Manager_Report"),
    path("Manager_Profile/", views.Manager_Profile, name="Manager_Profile"),
    path("Manager_Bookings/", views.Manager_Bookings, name="Manager_Bookings"),
    path("Manager_login/", views.Manager_login, name="Manager_login"),
    path("Request_Form/", views.Request_Form, name="Request_Form"),
    path("Feedback_Form/", views.Feedback_Form, name="Feedback_Form"),
    #path('', include("django.contrib.auth.urls")),

]
