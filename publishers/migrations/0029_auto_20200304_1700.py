# Generated by Django 2.1.7 on 2020-03-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0028_auto_20191126_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='references',
            field=models.TextField(blank=True, default='null', null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(default='null'),
        ),
    ]
