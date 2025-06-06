from django import template
from company.models import CompanyProfile

register = template.Library()

@register.filter
def has_company(user):
    return CompanyProfile.objects.filter(user=user).exists()
