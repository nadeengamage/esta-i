# Generated by Django 2.2.7 on 2019-11-12 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeaudittrail',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Employee'),
        ),
    ]
