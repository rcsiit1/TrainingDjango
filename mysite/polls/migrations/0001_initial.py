# Generated by Django 2.0.1 on 2018-01-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('designation', models.CharField(default='null', max_length=250)),
                ('department', models.CharField(default='null', max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]