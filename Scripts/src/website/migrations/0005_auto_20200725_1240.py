# Generated by Django 3.0.8 on 2020-07-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200724_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='AnalystNationalId',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='DoctorNationalId',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
