from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view', views.viewTicket, name='viewTicket'),
    path('search', views.searchTicket, name='searchTicket'),
    path('getzealdata', views.getAll, name='getAll'),
    path('message', views.postMsg, name='postMsg'),
]
