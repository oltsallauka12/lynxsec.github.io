# Generated by Django 5.1.5 on 2025-01-23 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_securityalert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('os', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], max_length=50)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cidr', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('deployed', 'Deployed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('last_health_check', models.DateTimeField(blank=True, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edr_instances', to='backoffice.host')),
            ],
        ),
        migrations.CreateModel(
            name='IDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('deployed', 'Deployed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('last_health_check', models.DateTimeField(blank=True, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ids_instances', to='backoffice.host')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ids_instances', to='backoffice.network')),
            ],
        ),
    ]
