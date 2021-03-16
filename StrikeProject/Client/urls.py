from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),

    path('logout/', views.logout_view, name='logout_view'),
    path('add-order/', views.addOrder, name='addOrder'),
    path('client-dashboard/', views.ClientDashboard, name='ClientDashboard'),
    path('order-history/', views.OrderHistory, name='OrderHistory'),
    # path('ngo-requirement-view/<int:rid>/', views.ngoRequirementView, name='ngoRequirementView'),
    # path('donor-requirement-view/<int:rid>/', views.donorRequirementView, name='donorRequirementView'),
    # path('donor-dashboard/', views.donorDashboard, name='donorDashboard'),
    # path('requirement-fulfillment/<int:rid>/', views.requirement_fulfillment, name='requirement_fulfillment'),




]