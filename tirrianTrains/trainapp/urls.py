from django.urls import path
from trainapp.views.customer import create_customer_view
from trainapp.views.booking import booking_page
from trainapp.views.maintenance import *

urlpatterns = [
    path('register/', create_customer_view, name='customer_creation'),
    path('booking/', booking_page, name='booking_page'),
    path('train/', get_trains, name="train_list"),
    path('train/<int:pk>/details', get_maintenance_history, name="train_detail"),
]