# Generated by Django 2.1.7 on 2019-08-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0002_auto_20190817_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='publisher/static/publishers'),
        ),
    ]
