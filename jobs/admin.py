from django.contrib import admin
from .models import Job, Application

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'created_at')
    search_fields = ('title', 'company_name')

admin.site.register(Job, JobAdmin)
admin.site.register(Application)