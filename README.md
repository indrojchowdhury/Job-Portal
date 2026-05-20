# Django-Job-Portal

This is a clean, modular, and fully-featured Job Portal web application built using **Django**. The project focuses heavily on backend logic, secure workflows, and dynamic frontend rendering using Django Templates.

---

## 📝 Project Summary

I built this Django-based job portal to manage job postings and applications efficiently. It features a custom user model supporting role-based authentication for **Job Seekers** and **Employers**. 

The system includes a complete workflow where employers can post and manage jobs, while job seekers can browse listings, upload resumes, and track their application status. To keep the app secure, I implemented strict permission-based access control and protected views. The entire frontend is rendered responsively using **Django Templates**, and the project is configured with deployment-ready settings for static and media file handling.

---

## 🛠️ Tools & Tech Stack Used

* **Backend Framework:** Django (MVC Architecture)
* **Database:** Relational Database with optimized relationships
* **Frontend Rendering:** Django Templates, HTML5, CSS3, and Responsive UI
* **File Storage:** Django Media handling (for secure Resume/PDF uploads)

---

## 🚀 Key Features Implemented

### 1. Custom User Model & Role Authentication
* **Role-Based Sign-up:** Separate registration, profiles, and dashboards for **Job Seekers** and **Employers**.
* **Custom User System:** Built extending Django’s BaseUserManager to cleanly handle user roles from the root.

### 2. Complete Job & Application Workflow
* **Job Posting & Management:** Employers can create, edit, and close job posts.
* **Browsing & Applying:** Job seekers can seamlessly view active jobs and apply by filling out forms and uploading their resumes.
* **Status Tracking:** An application management dashboard where employers can update application statuses (e.g., Pending, Reviewed, Shortlisted, Rejected).

### 3. Permissions & Security
* **Protected Views:** Used Django’s login decorators (`@login_required`) and mixins to prevent unauthorized users from accessing sensitive pages.
* **Access Control:** Ensured that job seekers cannot view applicant management lists and employers cannot apply for jobs.

### 4. Media & Static File Management
* **File Uploads:** Configured robust media file handling to process and store candidate resumes securely.
* **Deployment Ready:** Organized static assets (CSS, JS, Images) with proper production-ready settings.

---

## 🗺️ Core Core Web Routes (URL Roadmap)

| Module | URL Path | Method | Access Control | Description |
| :--- | :--- | :---: | :--- | :--- |
| **Auth** | `/accounts/signup/` | GET/POST | Public | Dynamic register page for Seekers/Employers |
| | `/accounts/login/` | GET/POST | Public | Standard login page |
| **Jobs** | `/jobs/` | GET | Public | Main job board showing all active listings |
| | `/jobs/create/` | GET/POST | Employer Only | Form to post a new job vacancy |
| | `/jobs/<id>/` | GET | Public | Detailed view of a single job opening |
| **Apply**| `/jobs/<id>/apply/` | GET/POST | Seeker Only | Application form page with resume upload |
| **Dashboard**| `/dashboard/` | GET | Authenticated | Personalized dashboard based on user role |
