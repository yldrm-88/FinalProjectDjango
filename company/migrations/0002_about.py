# Generated by Django 5.0.4 on 2024-05-16 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100, verbose_name='Başlık')),
                ('hakkimizda', models.TextField(max_length=2000, verbose_name='Hakkımızda')),
                ('resim', models.FileField(blank=True, null=True, upload_to='hakkimizda')),
            ],
        ),
    ]
