from django.urls import path
from .views import login, register, logout

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]