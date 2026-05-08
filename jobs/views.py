from django.shortcuts import render
from .models import Job
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application


# View to display all job listings
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_now(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    already_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    
    if not already_applied:
        Application.objects.create(job=job, applicant=request.user)
    
    return redirect('job_list')

@login_required
def dashboard(request):
    if request.user.is_employer:
        my_jobs = Job.objects.filter(employer=request.user)
        return render(request, 'jobs/employer_dashboard.html', {'jobs': my_jobs})
    else:
        applied_jobs = Application.objects.filter(applicant=request.user)
        return render(request, 'jobs/seeker_dashboard.html', {'applications': applied_jobs})