# jobs/views.py
from django.shortcuts import render
from .models import Job

# View to display all job listings
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})