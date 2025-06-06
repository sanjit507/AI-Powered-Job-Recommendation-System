from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, JobApplication

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_username',
            'placeholder': 'Enter your username',
            'required': 'required'
        }),
        error_messages={'unique': 'This username is already taken.'}
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_email',
            'placeholder': 'Enter your email address',
            'required': 'required'
        }),
        error_messages={'invalid': 'Please enter a valid email address.'}
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_first_name',
            'placeholder': 'Enter your first name',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_last_name',
            'placeholder': 'Enter your last name',
            'required': 'required'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'id_password1',
            'placeholder': 'Enter your password',
            'required': 'required'
        }),
        error_messages={'required': 'Please enter a password.'}
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'id_password2',
            'placeholder': 'Confirm your password',
            'required': 'required'
        }),
        error_messages={'required': 'Please confirm your password.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        """Ensure the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class ProfileSetupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'location', 'category', 'interests',
            'skills', 'education_level', 'avatar', 'resume'
        ]
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your job category'}),
            'interests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your interests'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your skills (comma-separated)'}),
            'education_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your education level'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
        }
        labels = {
            'avatar': 'Profile Picture',
            'resume': 'Upload Resume',
        }
        help_texts = {
            'skills': 'Enter a comma-separated list of your skills.',
            'resume': 'Upload your resume (PDF or DOCX).',
        }

    def clean_resume(self):
        """Validate that only PDF or DOCX files are uploaded."""
        resume = self.cleaned_data.get('resume')
        if resume:  # Check if a file is provided
            # Check the content type if available (for newly uploaded files)
            if hasattr(resume, 'file') and hasattr(resume.file, 'content_type'):
                content_type = resume.file.content_type
                allowed_content_types = [
                    'application/pdf',
                    'application/msword',
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                ]
                if content_type not in allowed_content_types:
                    raise forms.ValidationError("Only PDF or DOCX files are allowed.")
            else:
                # Fallback: Validate file extension if content_type is not available
                ext = resume.name.split('.')[-1].lower()
                if ext not in ['pdf', 'doc', 'docx']:
                    raise forms.ValidationError("Only PDF or DOCX files are allowed.")
        return resume


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['external_link_used']
        widgets = {
            'external_link_used': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the external link used for application (if any)'
            }),
        }
        labels = {
            'external_link_used': 'External Application Link',
        }

    def clean_external_link_used(self):
        """Validate the external link format."""
        external_link_used = self.cleaned_data.get('external_link_used')
        if external_link_used and not external_link_used.startswith(('http://', 'https://')):
            raise forms.ValidationError("Please enter a valid URL starting with 'http://' or 'https://'.")
        return external_link_used
    









