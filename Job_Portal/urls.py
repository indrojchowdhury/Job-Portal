
from django.contrib import admin
from django.urls import path, include
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('accounts.urls')),
    path('', include('jobs.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
]