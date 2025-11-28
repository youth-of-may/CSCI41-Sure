from django.shortcuts import render
from trainapp.services.customer_sql import create_customer
from django.http import HttpResponse

"""
imports the logic from trainapp and uses it to create a new customer
"""
def create_customer_view(request):  
    if request.method=='POST':
        if request.method == 'POST':
            cid = create_customer(request.POST['lastName'], request.POST['givenName'], request.POST.get('middleInitial'),request.POST['birthDate'], request.POST.get('gender'))
    return render(request, "trainapp/customer/customer_form.html")

def login_view(request):
    if request.method == 'POST':
        return HttpResponse("Work in Progress Hehe")
    else:
        return HttpResponse("Work in Progress hehe")
