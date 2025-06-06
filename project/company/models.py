from django.contrib.auth.models import User
from django.db import models

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    
    # In your CustomUser model
@property
def is_company(self):
    return hasattr(self, 'company')  # Assuming Company model has OneToOne with User

