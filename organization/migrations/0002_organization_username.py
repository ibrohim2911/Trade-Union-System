# Generated by Django 5.0.6 on 2024-05-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='username',
            field=models.CharField(default='user', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
