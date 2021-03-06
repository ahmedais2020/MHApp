# Generated by Django 3.0.8 on 2020-07-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200725_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='CenterCode',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='CenterName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='LabCode',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='LabName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='SynCode',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
