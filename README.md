# Django-Job-Portal

This is a fully-featured Job Portal web application built using **Python, Django, and MySQL**. The project focuses heavily on backend logic, secure workflows, dynamic frontend rendering using Django Templates, and it is fully deployed and ready for production.

---

## 📝 Project Summary

I built this Django-based job portal to manage job postings and applications efficiently. It features a custom user model supporting role-based authentication for **Job Seekers** and **Employers** using a **MySQL** database. 

The system includes a complete workflow where employers can post jobs, and job seekers can browse listings and apply by uploading their resumes. Employers can also easily view and download these resumes directly from their dashboard. To keep the app secure, I implemented strict permission-based access control and protected views. The entire frontend is responsive, built with **Django Templates**, and the project is fully deployed with proper media and static file handling.

---

## 🛠️ Tools & Tech Stack Used

* **Backend Framework:** Python & Django (MVC Architecture)
* **Database:** MySQL (Relational Database with optimized relationships)
* **Frontend Rendering:** Django Templates, HTML5, CSS3, and Responsive UI
* **File Storage:** Django Media handling (for secure Resume uploads and downloads)
* **Deployment:** Fully deployed and production-ready setup

---

## 🚀 Key Features Implemented

### 1. Custom User Model & Role Authentication
* **Role-Based Sign-up:** Separate registration, profiles, and dashboards for **Job Seekers** and **Employers**.
* **Custom User System:** Built using Django’s BaseUserManager to cleanly handle user roles from the root.

### 2. Job & Application Workflow (with Resume Handling)
* **Job Posting:** Employers can create, edit, and close job posts dynamically.
* **Resume Upload:** Job seekers can fill out forms and upload their resumes (PDF/Doc) when applying.
* **Resume Download:** Employers have full access to view and download applicant resumes directly from their management dashboard.
* **Status Tracking:** An application management system where employers can update status (e.g., Pending, Reviewed, Shortlisted, Rejected).

### 3. Permissions & Security
* **Protected Views:** Used Django’s login decorators (`@login_required`) and mixins to lock sensitive pages from guest users.
* **Access Control:** Job seekers cannot access employer management dashboards, and employers cannot apply for jobs.

### 4. Production Ready & Deployment
* **Media & Static Files:** Configured secure media storage to handle asset uploading and downloading without breaks.
* **Live Deployment:** Configured production-ready settings (`ALLOWED_HOSTS`, environment variables, static root) and successfully deployed the application.

---

## 🗺️ Core Web Routes (URL Roadmap)

| Module | URL Path | Method | Access Control | Description |
| :--- | :--- | :---: | :--- | :--- |
| **Auth** | `/accounts/signup/` | GET/POST | Public | Dynamic register page for Seekers/Employers |
| | `/accounts/login/` | GET/POST | Public | Standard login page |
| **Jobs** | `/jobs/` | GET | Public | Main job board showing all active listings |
| | `/jobs/create/` | GET/POST | Employer Only | Form to post a new job vacancy |
| | `/jobs/<id>/` | GET | Public | Detailed view of a single job opening |
| **Apply**| `/jobs/<id>/apply/` | GET/POST | Seeker Only | Application form page with resume upload |
| **Dashboard**| `/dashboard/` | GET | Authenticated | Personalized dashboard based on user role |
