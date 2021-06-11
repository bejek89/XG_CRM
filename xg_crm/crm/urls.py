# Widoki aplikacji crm
from django.urls import path
from .import views

app_name = 'crm'

urlpatterns = [
    path('', views.AllClientView.as_view(), name='clients'),
    path('all_tasks/', views.AllTaskView.as_view(), name='all_tasks'),
    path('new_tasks/', views.new_tasks_list, name='new_tasks'),
    path('ended_tasks/', views.ended_tasks_list, name='ended_tasks'),
    path('tasks_list_in_progress/', views.tasks_list_in_progress, name='tasks_list_in_progress'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_details/<int:client_id>', views.client_details, name='client_details'),
    path('phone_call/<int:client_id>', views.new_phone_call, name='phone_call'),
    path('task/<int:client_id>', views.new_task, name='new_task'),
    path('task_progress/<int:task_id>', views.task_progress, name='task_progress'),
    path('update_status/<int:task_id>', views.update_task_status, name='update_task_status')
]