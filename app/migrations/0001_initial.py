# Generated by Django 4.2.10 on 2024-02-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
