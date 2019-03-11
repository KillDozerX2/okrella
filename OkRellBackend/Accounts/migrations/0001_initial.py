# Generated by Django 2.1.5 on 2019-03-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(default='John', max_length=25, verbose_name='First Name')),
                ('last_name', models.CharField(default='Doe', max_length=25, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(default='johnDoe@okrella.com', max_length=255, unique=True, verbose_name='Email of user')),
                ('active', models.BooleanField(default=False, verbose_name='User is active')),
                ('staff', models.BooleanField(default=False, verbose_name='User is staff')),
                ('admin', models.BooleanField(default=False, verbose_name='User is admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]