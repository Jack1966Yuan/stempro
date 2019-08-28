# Generated by Django 2.2.1 on 2019-08-26 16:25

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200)),
                ('regular_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('member_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('start_date', models.DateField(blank=True)),
                ('adv_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('instructor', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InvolvedActive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200)),
                ('regular_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('member_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_date', models.DateField(blank=True)),
                ('adv_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200)),
                ('regular_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('member_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_date', models.DateField(blank=True)),
                ('adv_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterActive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_name', models.CharField(max_length=200)),
                ('who_register', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('register_date', models.DateField(default=datetime.date.today)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_email', models.CharField(max_length=200, unique=True)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('is_subscribed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TutorActive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('summary', models.TextField(blank=True, max_length=200)),
                ('regular_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('member_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_date', models.DateField(blank=True)),
                ('adv_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('type', models.CharField(blank=True, max_length=50)),
                ('related_account', models.CharField(blank=True, max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]