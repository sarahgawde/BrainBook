# Generated by Django 2.2.1 on 2019-05-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='snow.png', upload_to='profile_pics'),
        ),
    ]
