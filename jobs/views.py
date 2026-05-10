from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application, UserProfile
from django.contrib import messages

# Home Page (Welcome + Latest Jobs)
def home(request):
    latest_jobs = Job.objects.all().order_by('-created_at')[:5]
    return render(request, 'home.html', {'jobs': latest_jobs})

# Job List Page
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# Job Detail Page
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# Job Application (Cover Letter + Resume)
@login_required
def apply_now(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect('dashboard')

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        
        Application.objects.create(
            job=job,
            applicant=request.user,
            cover_letter=cover_letter,
            resume=resume
        )
        messages.success(request, "Applied Successfully!")
        return redirect('dashboard')

    return render(request, 'apply_form.html', {'job': job})

# Main Dashboard (Job Seeker + Employer)
@login_required
def dashboard(request):
    # If user is an employer, redirect to employer dashboard
    if hasattr(request.user, 'user_type') and request.user.user_type == 'employer':
        return redirect('employer_dashboard')
    
    # Otherwise, show Job Seeker Dashboard
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_at')
    return render(request, 'seeker_dashboard.html', {'applications': applications})

# Employer Dashboard (My Jobs + Applicants)
@login_required
def employer_dashboard(request):
    my_jobs = Job.objects.filter(employer=request.user).order_by('-created_at')
    all_applicants = Application.objects.filter(job__employer=request.user).order_by('-applied_at')
    
    context = {
        'my_jobs': my_jobs,
        'all_applicants': all_applicants,
    }
    return render(request, 'employer_dashboard.html', context)

# Application Status Update (Accept/Reject)
@login_required
def update_application_status(request, app_id, status):
    application = get_object_or_404(Application, id=app_id, job__employer=request.user)
    application.status = status
    application.save()
    messages.success(request, f"Application {status} successfully!")
    return redirect('employer_dashboard')

# Profile Management (Edit Profile + Upload Resume)
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.save()
        
        profile.phone = request.POST.get('phone')
        profile.bio = request.POST.get('bio')
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES.get('profile_picture')
        profile.save()
        
        messages.success(request, "Profile updated successfully!")
        return redirect('dashboard')
        
    return render(request, 'edit_profile.html', {'profile': profile})

@login_required
def create_job(request):
    # Only employers can post jobs
    if hasattr(request.user, 'user_type') and request.user.user_type != 'employer':
        return redirect('dashboard')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        company_name = request.POST.get('company_name')

        Job.objects.create(
            employer=request.user,
            title=title,
            description=description,
            location=location,
            salary=salary,
            company_name=company_name
        )
        messages.success(request, "Job posted successfully!")
        return redirect('employer_dashboard')

    return render(request, 'create_job.html')
