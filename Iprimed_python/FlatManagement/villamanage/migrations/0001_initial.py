# Generated by Django 3.2.6 on 2021-08-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Phn_no', models.CharField(max_length=50)),
                ('Email_id', models.CharField(max_length=50)),
            ],
        ),
    ]
