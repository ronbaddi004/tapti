# Generated by Django 2.2.4 on 2019-09-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapti_app', '0005_category_display_on_navbar'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='newly_added',
            field=models.BooleanField(default=False),
        ),
    ]
