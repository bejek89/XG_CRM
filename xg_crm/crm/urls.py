# Widoki aplikacji crm

from django.urls import path
from . import views


app_name = 'crm'

urlpatterns = [
    path('', views.AllClientView.as_view()),
    path('add_client/', views.add_client, name='add_client'),
    path('client_details/<int:client_id>', views.client_details,name='client_details'),
    path('phone_call/<int:client_id>', views.phone_call, name='phone_call'),
]