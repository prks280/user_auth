# Generated by Django 2.2.5 on 2019-09-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('ward_no', models.PositiveSmallIntegerField()),
            ],
        ),
    ]