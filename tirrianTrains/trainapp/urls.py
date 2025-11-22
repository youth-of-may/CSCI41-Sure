from django.urls import path
from trainapp.views.customer import create_customer

urlpatterns = [
    path('register/', create_customer, name='customer_creation'),
]