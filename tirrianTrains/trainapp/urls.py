from django.urls import path
from trainapp.views.customer import create_customer_view
from trainapp.views.booking import booking_page

urlpatterns = [
    path('register/', create_customer_view, name='customer_creation'),
    path('booking/', booking_page, name='booking_page'),
]