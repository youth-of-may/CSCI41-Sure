from django.shortcuts import render
from django.http import HttpResponse
from trainapp.services.customer_sql import create_customer

"""
imports the logic from trainapp and uses it to create a new customer
"""
def create_customer(request):  
    if request.method=='POST':
        if request.method == 'POST':
            cid = create_customer(
            request.POST['lastName'],
            request.POST['givenName'],
            request.POST.get('middleInitial'),
            request.POST['birthDate'],
            request.POST.get('gender')
            )
    return render(request, "trainapp/customer_form.html")
