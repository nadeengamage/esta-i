# Generated by Django 2.2.7 on 2019-11-13 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0003_delete_employeeaudittrail'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('emp_id', models.IntegerField(blank=True, db_index=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('working_hours', models.TimeField()),
                ('date_join', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True, verbose_name='Left Date')),
                ('status', models.BooleanField(verbose_name='Employee Active Status')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical employee',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
