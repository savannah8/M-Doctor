# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-11 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('time_slot', models.CharField(choices=[('6', '6:00 am'), ('7', '7:00 am'), ('8', '8:00 am'), ('9', '9:00 am'), ('10', '10:00 am'), ('11', '11:00 am'), ('12', '12:00 am'), ('13', '1:00 pm'), ('14', '2:00 pm'), ('15', '3:00 pm'), ('16', '4:00 pm'), ('17', '5:00 pm'), ('18', '6:00 pm')], max_length=20, null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='chemoapp.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.FileField(default='default.jpg', null=True, upload_to='images')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('consultation_fee', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('registration_number', models.CharField(max_length=100)),
                ('registration_date', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('facility', models.CharField(max_length=100)),
                ('postal_address', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('sub_speciality', models.CharField(max_length=100)),
                ('qualifications', models.CharField(max_length=100)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='chemoapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Doctor')),
            ],
            options={
                'verbose_name_plural': 'Doctor reviews',
            },
        ),
        migrations.CreateModel(
            name='DoctorSpeciality',
            fields=[
                ('specialty', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Doctors specialties',
            },
        ),
        migrations.CreateModel(
            name='DoctorWorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_from', models.CharField(choices=[('6', '6:00 am'), ('7', '7:00 am'), ('8', '8:00 am'), ('9', '9:00 am'), ('10', '10:00 am'), ('11', '11:00 am'), ('12', '12:00 am'), ('13', '1:00 pm'), ('14', '2:00 pm'), ('15', '3:00 pm'), ('16', '4:00 pm'), ('17', '5:00 pm'), ('18', '6:00 pm')], max_length=20)),
                ('working_to', models.CharField(choices=[('6', '6:00 am'), ('7', '7:00 am'), ('8', '8:00 am'), ('9', '9:00 am'), ('10', '10:00 am'), ('11', '11:00 am'), ('12', '12:00 am'), ('13', '1:00 pm'), ('14', '2:00 pm'), ('15', '3:00 pm'), ('16', '4:00 pm'), ('17', '5:00 pm'), ('18', '6:00 pm')], max_length=20)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='working_hours', to='chemoapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='LiveChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField()),
                ('pinned_message', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.FileField(default='default.jpg', null=True, upload_to='images')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('id_number', models.CharField(max_length=8, unique=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('doctors', models.ManyToManyField(to='chemoapp.Doctor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='livechat',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Patient'),
        ),
        migrations.AddField(
            model_name='doctorreview',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Patient'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.DoctorSpeciality'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='chemoapp.Posts'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='chemoapp.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chemoapp.Patient'),
        ),
    ]
