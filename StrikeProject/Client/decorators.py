from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from .models import *
from django.contrib import messages

def is_logged(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')

                # group = Group.objects.get(user = request.user)
                # if group.name == 'donor':   
                #     return redirect('donorDashboard')
                # else:
                #     return redirect('ngoDashboard')
            else:
                
                return view_func(request, *args, **kwargs)
        return wrapper_func 
    


# def ngo_required(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = Group.objects.get(user = request.user)
#         if group.name == 'ngo':
#             return view_func(request, *args, **kwargs)
#         else:
#             return HttpResponse('You are not authorized to view this page.')
#     return wrapper_func 


# def donor_required(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = Group.objects.get(user = request.user)
#         if group.name == 'donor':
#             return view_func(request, *args, **kwargs)
#         else:
#             return HttpResponse('You are not authorized to view this page.')
#     return wrapper_func 




# def adminprofile_required(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         profile = Admin.objects.filter(user = request.user).count()
#         if profile == 0:
#             return redirect('adminProfile')
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper_func 


# def studentprofile_required(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         profile = Student.objects.filter(user = request.user).count()
#         if profile == 0:
#             return redirect('studentProfile')
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper_func 