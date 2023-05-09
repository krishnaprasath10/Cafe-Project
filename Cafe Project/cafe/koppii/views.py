from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib import messages 
from django.http import JsonResponse
import json



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

def service(request):
    return render(request, 'service.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, "login.html")

def cart(request):
    return render(request, "cart.html")

def in_reservation(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        person = request.POST['person']

        user = Reservations.objects.filter(Date=date, Time=time)

        if user:
            messages.warning(request, "Already Booked")
            return render(request, "reservation.html")
        else:
            new = Reservations.objects.create(
                Name=name, Email=email, Date=date, Time=time, Person=person)
            #messag = "Reservation Succesfully"
            messages.success(request, "reservation successfully")
            return render(request, "reservation.html")


def in_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new = Contacts.objects.create(
            Name=name, Email=email, Subject=subject, Message=message)
        return render(request, "contact.html")


def in_signin(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        user = signins.objects.filter(Email=email)
        if user:
            message = "Email Already Exits"
            return render(request, "signin.html", {'msg': message})
        else:
            if password == conpassword:
                new = signins.objects.create(
                    Name=name, Email=email, Contact=contact, Password=password)

                message = "Signin Succesfully.Please"
                return render(request, "login.html", {'msgg': message})
            else:
                message = "Password And Confirm Password Are Not Same"
                return render(request, "signin.html", {'msg': message})


def in_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            pwd = request.POST.get('password')
            user = authenticate(request, email=email, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("/login")
        return render(request, "login.html")


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        message = "Logout Succesfull"
        return render(request, 'login.html', {'msg': message})

def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            # print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status': 'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request, "cart.html", {"cart": cart})
    else:
        return redirect("/")
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")