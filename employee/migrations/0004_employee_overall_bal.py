# Generated by Django 4.0 on 2024-05-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_children'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='overall_bal',
            field=models.IntegerField(default=0),
        ),
    ]
