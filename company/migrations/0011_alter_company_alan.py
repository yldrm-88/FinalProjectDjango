# Generated by Django 5.0.4 on 2024-05-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_alan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='alan',
            field=models.CharField(max_length=50),
        ),
    ]
