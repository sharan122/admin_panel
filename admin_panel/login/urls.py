from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.printerr),
    path('vaishnav/',views.vaishnav)
    
]
