from django.shortcuts import render, redirect
from trainapp.services.customer_sql import create_customer, query_customer
from django.contrib import messages
from django.db import IntegrityError

def create_customer_view(request):  
    if request.method == 'POST':
        email = request.POST.get('email')

        if query_customer(email):
            messages.error(request, "Email already exists. Please use another email.")
            return render(request, "trainapp/customer/customer_form.html")

        try:
            create_customer(
                request.POST['lastName'],
                request.POST['givenName'],
                request.POST.get('middleInitial'),
                request.POST['birthDate'],
                request.POST.get('gender'),
                email
            )
            return redirect("homepage")

        except IntegrityError:
            messages.error(request, "That email is already registered.")
            return render(request, "trainapp/customer/customer_form.html")

    return render(request, "trainapp/customer/customer_form.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        
        user = query_customer(email)
        if user:
            request.session["customer_id"] = user["customerID"]
            return redirect("homepage")
        # If unsuccessful login
        return render(request, "trainapp/customer/customer_login.html", {"error": "Invalid credentials"})
    else:
        return render(request, "trainapp/customer/customer_login.html")
    
def logout(request):
    request.session.flush()
    return redirect('login')