# Generated by Django 4.2.1 on 2023-08-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_heck_box_article_multiple_check_box_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='heck_box',
            new_name='check_box',
        ),
    ]