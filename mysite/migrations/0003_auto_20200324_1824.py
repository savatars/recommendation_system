# Generated by Django 2.1 on 2020-03-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200319_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='event',
        ),
        migrations.RemoveField(
            model_name='features',
            name='itemid',
        ),
        migrations.RemoveField(
            model_name='features',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='features',
            name='visitorid',
        ),
        migrations.AddField(
            model_name='features',
            name='customerid',
            field=models.CharField(default='0000000', editable=False, max_length=7),
        ),
        migrations.AddField(
            model_name='features',
            name='recommendedProducts',
            field=models.TextField(default='-'),
        ),
    ]
