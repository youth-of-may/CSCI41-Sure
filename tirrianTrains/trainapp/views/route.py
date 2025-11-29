from django.shortcuts import render, redirect
from trainapp.services.station_sql import *
from trainapp.services.route_sql import *
from trainapp.services.price_history_sql import *
from django.http import HttpResponse
from django.contrib import messages


def stations_list(request):
    context = {
        'local_station': list_stations(True),
        'intertown_station': list_stations(False),
    }
    return render(request, "trainapp/stations/station_list.html", context)

def station_detail(request, destinationID, routeType):
    if routeType == ("local"):
        routeParameter = 1
    else:
        routeParameter = 0
    
    context = {
        'station_name': get_station_name(destinationID),
        'routes': filter_destination_routes(destinationID, routeParameter)
    }
    return render(request, "trainapp/stations/station_detail.html", context)

def stations_add(request):
    if request.method == 'POST':
        create_station(request.POST['stationName'])
        return redirect('station_list')
        
    return render(request,"trainapp/stations/station_create.html")

def routes_add(request):
    context = {
        'stations': list_stations()
    }
    if request.method == "POST":
        originID = request.POST.get("originID")
        destID = request.POST.get("destID")
        baseCost = request.POST.get("baseCost")
        isLocalRoute = request.POST.get("isLocalRoute")
        estDuration = request.POST.get("estDuration")
        if originID == destID:
            messages.error(request, "Origin and destination cannot be the same station.")
            return redirect("route_create")

        try:
            add_route(originID, destID, baseCost, isLocalRoute, estDuration)
            return redirect("station_detail", destinationID=destID) 
        except Exception as e:
            messages.error(request, f"Database error: {str(e)}")
            return redirect("route_create")
    return render(request, "trainapp/stations/route_create.html", context)


def route_price_history(request, routeID):
    ''' Show the price changes made on a specific route '''
    context ={
        'routePriceHistory': generate_price_history(routeID),
        'routeInfo': get_route_info(routeID),
    }
    return render(request, "trainapp/price/price_history.html",context)

def change_route_price(request, routeID):
    ''' Change the base price of a route '''
    if request.method == 'POST':
        new_price = request.POST.get("price")
        
        # Basic input cleaning
        if not new_price or not new_price.isdigit():
            return HttpResponse("Invalid Price")
        
        new_price = int(new_price)
        
        update_route_price(routeID, new_price)
        return redirect('route_price_history', routeID=routeID)
    else:
        return render(request, "trainapp/price/price_change.html")