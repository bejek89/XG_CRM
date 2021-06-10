# Widoki aplikacji crm
from django.urls import path
from .import views

app_name = 'crm'

urlpatterns = [
    path('', views.AllClientView.as_view(), name='clients'),
    path('all_tasks/', views.AllTaskView.as_view(), name='all_tasks'),
    path('new_tasks/', views.AllTaskView.as_view(), name='new_task'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_details/<int:client_id>', views.client_details, name='client_details'),
    path('phone_call/<int:client_id>', views.new_phone_call, name='phone_call'),
    path('task/<int:client_id>', views.new_task, name='new_task'),
    path('task_progress/<int:task_id>', views.task_progres, name='task_progres')
]