# Generated by Django 4.2.5 on 2023-11-02 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_staff_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvideos',
            name='video_description_arm',
        ),
        migrations.RemoveField(
            model_name='productvideos',
            name='video_description_eng',
        ),
    ]