
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', views.hello),
]
