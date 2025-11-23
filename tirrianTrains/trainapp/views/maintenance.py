from django.shortcuts import render
from trainapp.services.maintenance_sql import *


def get_trains(request):
    context = {
        'train': list_trains()
    }
    return render(request, "trainapp/train_maintenance/train_maintenance_list.html", context)

def get_maintenance_history(request, pk):
    context = {
        'train_details': get_train_details(pk),
        'maintenance_history': get_train_maintenance(pk)
    }
    return render(request, "trainapp/train_maintenance/train_maintenance_detail.html", context)