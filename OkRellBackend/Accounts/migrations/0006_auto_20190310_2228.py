# Generated by Django 2.1.5 on 2019-03-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_remove_siteuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of birth'),
        ),
    ]
