# Generated by Django 3.2.6 on 2021-08-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villamanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villa',
            name='package',
            field=models.CharField(default=False, max_length=50),
        ),
    ]