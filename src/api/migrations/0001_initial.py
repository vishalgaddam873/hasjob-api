# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 13:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_salary', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999, message='Please Check you Enter Correct Salary or not')])),
                ('job_related_experince', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_type', models.CharField(blank=True, choices=[('FULL-TIME EMPLOYMENT', 'Full-time employment'), ('SHORT-TERM CONTRACT', 'Short-term contract'), ('INTERNSHIP', 'Internship'), ('FREELANCE OR CONSULTING', 'Freelance or consulting'), ('VOLUNTEER CONTRIBUTOR', 'Volunteer contributor'), ('PARTNER FOR A VENTURE', 'Partner for a venture')], max_length=50)),
                ('job_category', models.CharField(blank=True, choices=[('PROGRAMMING', 'Programming'), ('GRAPHIC DESIGN', 'Graphic Design'), ('ELECTORINCS', 'Electornics'), ('TESTING', 'Testing')], max_length=50)),
                ('job_location', models.CharField(blank=True, choices=[('ANYWHERE', 'Anywhere'), ('BANGLORE', 'Banglore, IN'), ('CHENNAI', 'Channai, IN'), ('MUMBAI', 'Mumbai, IN'), ('PUNE', 'Pune, IN')], max_length=50, null=True)),
                ('job_description', models.TextField(blank=True)),
                ('salary', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999, message='Enter correct salary')])),
                ('skill_requirements', models.TextField(blank=True, null=True)),
                ('job_preks', models.TextField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=80)),
                ('date_of_post', models.DateField(auto_now_add=True)),
                ('Employee_Detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=50)),
                ('contact_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999, message='Please enter correct Mobile number')])),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('experience', models.CharField(default='Fresher', max_length=30)),
                ('resume_url', models.URLField()),
                ('proffession', models.CharField(max_length=100)),
                ('current_or_pervious_company_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]