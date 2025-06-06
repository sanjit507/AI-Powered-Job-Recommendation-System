from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export import resources  
from import_export.admin import ImportExportMixin

# ========== Job Admin ==========
class JobResource(resources.ModelResource):
    class Meta:
        model = Job
        fields = (
            "id", "title", "description", "company", "location", "category",
            "created_date", "deadline", "salary", "requirements", "responsibilities",
            "contact_email", "required_skills", "education_level"
        )
        import_id_fields = ['id']

class JobAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = JobResource
    list_display = ('title', 'company', 'location', 'category', 'created_date', 'deadline', 'salary')
    list_filter = ('category', 'location', 'created_date')
    search_fields = ('title', 'description', 'company', 'requirements', 'responsibilities')
    list_editable = ('category',)
    readonly_fields = ('created_date', 'image_tag')
    date_hierarchy = 'created_date'
    list_per_page = 10

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:100px;max-height:100px;" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

admin.site.register(Job, JobAdmin)

# ========== JobApplication Admin ==========
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'job', 'applied_on', 'status', 'interview_meeting_link', 'interview_message_short'
    )
    list_per_page = 15
    list_filter = ('job', 'applied_on', 'status')
    search_fields = ('user__username', 'job__title')
    list_editable = ('status',)
    readonly_fields = ('applied_on',)

    fieldsets = (
        (None, {
            'fields': (
                'user', 'job', 'applied_on', 'application_method', 'external_link_used', 'status',
                'interview_meeting_link', 'interview_message'
            )
        }),
    )

    def interview_message_short(self, obj):
        return (obj.interview_message[:50] + '...') if obj.interview_message else ''
    interview_message_short.short_description = 'Interview Message'

# ========== UserProfile Admin ==========
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'category', 'education_level', 'skills')
    search_fields = ('user__username', 'location', 'category', 'skills')
    list_filter = ('category', 'education_level')
    readonly_fields = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
