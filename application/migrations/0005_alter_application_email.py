# Generated by Django 4.0.5 on 2022-09-15 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_application_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='email'),
        ),
    ]
