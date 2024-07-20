# Generated by Django 5.0.6 on 2024-07-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='wholesaler',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
