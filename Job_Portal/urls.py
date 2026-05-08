# job_portal_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.name),
    path('accounts/', include('accounts.urls')), # For login/register
    path('', include('jobs.urls')), # Main job related pages
]