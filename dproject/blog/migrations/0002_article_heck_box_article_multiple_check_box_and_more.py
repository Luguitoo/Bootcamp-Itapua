# Generated by Django 4.2.1 on 2023-08-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='heck_box',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='multiple_check_box',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='pulldown',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='radio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]