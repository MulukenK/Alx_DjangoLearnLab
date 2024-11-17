from django.shortcuts import render

# Create your views here.
# views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import YourModel

@permission_required('yourapp.can_view', raise_exception=True)
def view_instance(request, instance_id):
    instance = YourModel.objects.get(id=instance_id)
    return render(request, 'yourapp/view_instance.html', {'instance': instance})

@permission_required('yourapp.can_create', raise_exception=True)
def create_instance(request):
    if request.method == "POST":
        # Code to create a new instance
        return redirect('view_instance', instance_id=new_instance.id)
    return render(request, 'yourapp/create_instance.html')

@permission_required('yourapp.can_edit', raise_exception=True)
def edit_instance(request, instance_id):
    instance = YourModel.objects.get(id=instance_id)
    if request.method == "POST":
        # Code to edit instance
        return redirect('view_instance', instance_id=instance.id)
    return render(request, 'yourapp/edit_instance.html', {'instance': instance})

@permission_required('yourapp.can_delete', raise_exception=True)
def delete_instance(request, instance_id):
    instance = YourModel.objects.get(id=instance_id)
    instance.delete()
    return HttpResponse("Instance deleted")