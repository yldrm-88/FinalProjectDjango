# Generated by Django 5.0.4 on 2024-05-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_company_alan_alter_student_alan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bolum',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='student',
            name='bolum',
            field=models.CharField(max_length=35),
        ),
    ]