from django.urls import path
from trainapp.views.customer import create_customer_view
from trainapp.views.booking import booking_page
from trainapp.views.maintenance import *
from trainapp.views.trips import *
from trainapp.views.route import *
from trainapp.views.admin_views import *

urlpatterns = [
    path('register/', create_customer_view, name='customer_creation'),
    path('booking/', booking_page, name='booking_page'),
    path('maintenance/add', maintenance_add, name="maintenance_add"),
    path('train/<int:pk>/details', get_maintenance_history, name="train_detail"),
    path('trips/', schedules_list, name="schedule_list"),
    path('trips/<str:trip_date>/details', schedule_detail, name="schedule_detail"),
    path('stations/', stations_list, name="station_list"),
    path('stations/add', stations_add, name="station_create"),
    path('stations/<int:destinationID>/details', station_detail, name="station_detail"),
    path('routes/<int:routeID>/price_history', route_price_history, name="route_price_history"),
    path('tirian/admin', admin_details, name="tirian_admin"),
]