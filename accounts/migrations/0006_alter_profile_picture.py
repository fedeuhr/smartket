# Generated by Django 3.2.6 on 2022-01-16 17:08

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default_user.jpg', upload_to=accounts.models.user_directory_path_profile),
        ),
    ]
