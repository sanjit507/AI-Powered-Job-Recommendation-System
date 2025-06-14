# Generated by Django 6.0 on 2025-03-20 11:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_remove_userprofile_photo"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="contact_email",
            field=models.EmailField(
                help_text="Contact email for job inquiries", max_length=254
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="created_date",
            field=models.DateField(
                default=django.utils.timezone.now, help_text="Date the job was posted"
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="deadline",
            field=models.DateField(help_text="Application deadline for the job"),
        ),
        migrations.AlterField(
            model_name="job",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Job-related image",
                null=True,
                upload_to="job_images/",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="requirements",
            field=models.TextField(
                help_text="Skills or qualifications required for the job"
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="responsibilities",
            field=models.TextField(help_text="Key responsibilities for the job"),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Salary offered for the job",
                max_digits=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="application_method",
            field=models.CharField(
                choices=[
                    ("PLATFORM", "Applied via Platform"),
                    ("LINK", "Applied via External Link"),
                ],
                default="PLATFORM",
                help_text="Method used to apply for the job",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="applied_on",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Timestamp when the application was submitted",
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="app.job",
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="category",
            field=models.CharField(
                blank=True,
                help_text="Preferred job category",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="location",
            field=models.CharField(
                blank=True, help_text="User's location", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
