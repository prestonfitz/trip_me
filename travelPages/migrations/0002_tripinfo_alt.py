# Generated by Django 4.1.7 on 2023-05-04 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelPages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripinfo',
            name='alt',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
