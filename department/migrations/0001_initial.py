# Generated by Django 2.2.7 on 2019-12-05 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('working_days_per_week', models.IntegerField()),
                ('working_hours_per_day', models.TimeField()),
                ('status', models.BooleanField(verbose_name='Department active status')),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='DepartmentHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('working_days_per_week', models.IntegerField()),
                ('working_hours_per_day', models.TimeField()),
                ('status', models.BooleanField()),
                ('history_change_reason', models.CharField(max_length=50)),
                ('history_type', models.CharField(max_length=10)),
                ('history_date', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(db_column='dep_id', on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
            options={
                'db_table': 'department_audit_trail',
            },
        ),
    ]
