from django.shortcuts import render
from trainapp.services.trips_sql import *


def schedules_list(request):
    context = {
        'schedule': list_trips_per_date()
    }
    return render(request, "trainapp/trip_schedule/trips_list.html", context)

def schedule_detail(request, trip_date):
    context = {
        'date':get_raw_date(trip_date),
        'local': list_local_intertown(True, trip_date),
        'intertown': list_local_intertown(False, trip_date)
    }
    return render(request, "trainapp/trip_schedule/trips_detail.html", context)