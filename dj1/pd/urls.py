from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pd import views

urlpatterns = [
    path('flask/',views.flask),
    path('pyramid/',views.pyramid),
    path('django/',views.django),
]