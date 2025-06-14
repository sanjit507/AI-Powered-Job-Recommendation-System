# Generated by Django 5.1.7 on 2025-03-11 19:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_profile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="job",
            options={},
        ),
        migrations.AlterModelOptions(
            name="jobapplication",
            options={},
        ),
        migrations.RemoveField(
            model_name="job",
            name="experience_years",
        ),
        migrations.RemoveField(
            model_name="job",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="jobapplication",
            name="cover_letter",
        ),
        migrations.RemoveField(
            model_name="jobapplication",
            name="resume",
        ),
        migrations.RemoveField(
            model_name="jobapplication",
            name="status",
        ),
        migrations.AlterField(
            model_name="job",
            name="apply_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="category",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="company",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="contact_email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="job",
            name="created_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="job",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="education_level",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="job_images"),
        ),
        migrations.AlterField(
            model_name="job",
            name="location",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="job",
            name="required_skills",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="requirements",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="responsibilities",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(max_length=255),
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
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="applied_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="external_link_used",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.job"
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
