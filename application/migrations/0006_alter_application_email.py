# Generated by Django 4.0.5 on 2022-09-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_application_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='email'),
        ),
    ]
