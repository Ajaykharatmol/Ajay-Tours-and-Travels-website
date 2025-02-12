from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path('about',views.about,name="about"),
    path("contact2", views.contact2, name="contact2"),
    path('contact',views.contact,name="contact"),
    path("service", views.service, name="service"),
    path('cars',views.cars,name="cars"),
    path('feature',views.feature,name="feature"),
   
]