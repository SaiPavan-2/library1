# Generated by Django 4.0.3 on 2022-11-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_papers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='paper',
            field=models.FileField(upload_to='static/'),
        ),
    ]