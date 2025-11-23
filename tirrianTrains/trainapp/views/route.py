from django.shortcuts import render
from trainapp.services.station_sql import *
from trainapp.services.route_sql import *


def stations_list(request):
    context = {
        'local_station': list_stations(True),
        'intertown_station': list_stations(False),
    }
    return render(request, "trainapp/stations/station_list.html", context)

def station_detail(request, destinationID):
    context = {
        'station_name': get_station_name(destinationID),
        'routes': get_destination_routes(destinationID),
    }
    return render(request, "trainapp/stations/station_detail.html", context)