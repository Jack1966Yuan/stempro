# Generated by Django 2.2.1 on 2019-09-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190903_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribePresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('cellphone', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('wechat', models.CharField(blank=True, max_length=200, null=True)),
                ('schoolName', models.CharField(max_length=200)),
            ],
        ),
    ]
