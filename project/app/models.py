from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='job_images/', null=True, blank=True, help_text="Job-related image")
    created_date = models.DateField(default=timezone.now, help_text="Date the job was posted")
    deadline = models.DateField(help_text="Application deadline for the job")
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Salary offered for the job")
    requirements = models.TextField(help_text="Skills")
    responsibilities = models.TextField(help_text="Key responsibilities for the job")
    contact_email = models.EmailField(help_text="Contact email for job inquiries")
    required_skills = models.TextField(help_text="Comma-separated list of required skills")
    education_level = models.CharField(max_length=255, help_text="Minimum education level required")
    apply_link = models.URLField(null=True, blank=True, help_text="Link to apply externally")

    def __str__(self):
        return self.title

    def has_official_website(self):
        """Check if the job has an official website."""
        return bool(self.apply_link)


class JobApplication(models.Model):
    APPLICATION_METHOD_CHOICES = [
        ('PLATFORM', 'Applied via Platform'),
        ('LINK', 'Applied via External Link'),
    ]

    APPLICATION_STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('IN_REVIEW', 'In Review'),
        ('INTERVIEW', 'Interview'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_on = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the application was submitted")
    application_method = models.CharField(
        max_length=10,
        choices=APPLICATION_METHOD_CHOICES,
        default='PLATFORM',
        help_text="Method used to apply for the job"
    )
    external_link_used = models.URLField(null=True, blank=True, help_text="External link used for application")
    status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='APPLIED',
        help_text="Current status of the job application"
    )
    
    # 🔽 New Fields
    interview_meeting_link = models.URLField(
        null=True,
        blank=True,
        help_text="Meeting link for interview (e.g., Zoom, Google Meet)"
    )
    interview_message = models.TextField(
        null=True,
        blank=True,
        help_text="Message or instructions about the interview"
    )

    def __str__(self):
        return f"{self.user.username} - {self.job.title} - {self.get_status_display()}"

    def save(self, *args, **kwargs):
        # Automatically set the application method based on whether an external link is used
        if self.external_link_used:
            self.application_method = 'LINK'
        else:
            self.application_method = 'PLATFORM'
        super().save(*args, **kwargs)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=255, blank=True, null=True, help_text="User's location")
    category = models.CharField(max_length=255, blank=True, null=True, help_text="Preferred job category")
    interests = models.TextField(blank=True, null=True, help_text="User's interests")
    skills = models.TextField(blank=True, null=True, help_text="Comma-separated list of skills")
    education_level = models.CharField(max_length=255, blank=True, null=True, help_text="User's highest education level")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="User's profile picture")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, help_text="User's resume (PDF or DOCX)")

    def __str__(self):
        return self.user.username
