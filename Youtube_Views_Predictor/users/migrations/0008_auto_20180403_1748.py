# Generated by Django 2.0.2 on 2018-04-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180401_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_channel_sub',
            name='date1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video_main',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video_sub',
            name='date1',
            field=models.CharField(max_length=100),
        ),
    ]