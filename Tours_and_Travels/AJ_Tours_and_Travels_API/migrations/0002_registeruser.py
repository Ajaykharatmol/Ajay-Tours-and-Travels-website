# Generated by Django 5.1.4 on 2025-01-30 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AJ_Tours_and_Travels_API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=500, null=True, validators=[django.core.validators.RegexValidator(message="Email Id must be entered in the format: example326@gmail.com' Up to 50 character allowed.", regex='^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$')])),
                ('password', models.CharField(max_length=20, null=True)),
                ('profile_image', models.FileField(null=True, upload_to='images/profile_images/')),
                ('mob_no', models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999',0989279999 Up to 14 digits allowed.", regex='^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$')])),
                ('OTP', models.IntegerField(null=True)),
                ('fb_check', models.CharField(max_length=500, null=True)),
                ('loc_latitude', models.FloatField(null=True)),
                ('loc_longitude', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
