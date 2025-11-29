from django.shortcuts import render, redirect
from trainapp.services.maintenance_sql import *



def get_maintenance_history(request, pk):
    context = {
        'train_details': get_train_details(pk),
        'maintenance_history': get_train_maintenance(pk)
    }
    return render(request, "trainapp/train_maintenance/train_maintenance_detail.html", context)

def maintenance_add(request):
    context = {
        'trains': list_trains()
    }
    if request.method == 'POST':
        id = request.POST['train']
        add_maintenance(id, request.POST['maintenanceDate'], 
                        request.POST['crew'], request.POST['task'], request.POST['train_condition'], )
        return redirect('train_detail', pk=id)
        
    return render(request,"trainapp/train_maintenance/train_maintenance_create.html", context)
