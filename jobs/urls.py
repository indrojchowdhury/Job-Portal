# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_now, name='apply_now'),
]