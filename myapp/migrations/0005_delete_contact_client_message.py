# Generated by Django 5.1.2 on 2024-12-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contact_remove_attendance_class_attended_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='client',
            name='message',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
