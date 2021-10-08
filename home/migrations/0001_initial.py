# Generated by Django 3.2.7 on 2021-09-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slider_Name', models.CharField(max_length=50)),
                ('Slider_Path', models.CharField(max_length=200)),
                ('Slider_Status', models.BooleanField(default=False)),
                ('Slide_Message', models.CharField(max_length=100)),
            ],
        ),
    ]
