from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-jobs/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_now, name='apply_now'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply/<int:job_id>/', views.apply_now, name='apply_now'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('update-status/<int:app_id>/<str:status>/', views.update_application_status, name='update_status'),
    path('post-job/', views.create_job, name='create_job'),
]
