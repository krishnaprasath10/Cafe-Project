# Generated by Django 4.1.5 on 2023-03-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Date', models.CharField(max_length=50)),
                ('Time', models.CharField(max_length=50)),
                ('Person', models.CharField(max_length=50)),
            ],
        ),
    ]
