# Generated by Django 2.2.7 on 2019-12-11 08:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identity_no', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('working_hours', models.TimeField()),
                ('department', models.ForeignKey(db_column='dep_id', on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
                ('employee', models.ForeignKey(db_column='emp_id', on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            options={
                'db_table': 'assigner',
            },
        ),
        migrations.CreateModel(
            name='AssignerHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('working_hours', models.TimeField()),
                ('history_change_reason', models.CharField(max_length=50)),
                ('history_type', models.CharField(max_length=10)),
                ('history_date', models.DateTimeField(auto_now_add=True)),
                ('assigner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assigner.Assigner')),
                ('department', models.ForeignKey(db_column='dep_id', on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
                ('employee', models.ForeignKey(db_column='emp_id', on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            options={
                'db_table': 'assigner_audit_trail',
            },
        ),
    ]
