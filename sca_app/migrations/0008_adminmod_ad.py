# Generated by Django 5.0.3 on 2024-05-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sca_app', '0007_rename_admin_adminmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminmod',
            name='ad',
            field=models.BooleanField(default=True),
        ),
    ]
