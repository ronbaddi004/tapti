# Generated by Django 2.2.4 on 2019-09-10 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tapti_app', '0007_auto_20190909_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newly_arrival', models.BooleanField(default=False)),
                ('image', models.FileField(upload_to='images/')),
                ('header', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('my_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tapti_app.Item')),
            ],
        ),
    ]