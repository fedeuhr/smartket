# Generated by Django 3.2.9 on 2021-12-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
