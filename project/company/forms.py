from django import forms
from django.contrib.auth.models import User
from .models import CompanyProfile

class CompanyRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    industry = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    company_name = forms.CharField(max_length=100)
    website = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            CompanyProfile.objects.create(
                user=user,
                email=self.cleaned_data['email'],
                industry=self.cleaned_data['industry'],
                location=self.cleaned_data['location'],
                company_name=self.cleaned_data['company_name'],
                website=self.cleaned_data['website']
            )
        return user
