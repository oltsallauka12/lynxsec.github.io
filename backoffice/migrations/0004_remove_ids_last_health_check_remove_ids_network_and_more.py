# Generated by Django 5.1.5 on 2025-01-23 23:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_host_network_edr_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ids',
            name='last_health_check',
        ),
        migrations.RemoveField(
            model_name='ids',
            name='network',
        ),
        migrations.RemoveField(
            model_name='ids',
            name='status',
        ),
        migrations.AddField(
            model_name='ids',
            name='configuration',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ids',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ids',
            name='deployment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('deployed', 'Deployed'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
    ]
