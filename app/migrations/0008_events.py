# Generated by Django 2.2.1 on 2019-10-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190922_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=2000)),
                ('capacity', models.IntegerField()),
                ('when', models.DateTimeField()),
            ],
        ),
    ]