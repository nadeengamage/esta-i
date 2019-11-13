# Generated by Django 2.2.7 on 2019-11-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('working_hours', models.TimeField()),
                ('date_join', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True, verbose_name='Left Date')),
                ('status', models.BooleanField(verbose_name='Employee Active Status')),
            ],
            options={
                'db_table': 'employee',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeAuditTrail',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('working_hours', models.TimeField()),
                ('date_join', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True, verbose_name='Left Date')),
                ('status', models.BooleanField(verbose_name='Employee Active Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp_audit_id', to='employee.Employee')),
            ],
            options={
                'db_table': 'employee_audit_trail',
                'ordering': ['-pk'],
            },
        ),
    ]
