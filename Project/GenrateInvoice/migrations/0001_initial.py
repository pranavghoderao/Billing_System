# Generated by Django 3.0.6 on 2020-05-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('panNo', models.CharField(max_length=10)),
                ('Gstin', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customerdetails',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=100)),
                ('prodCode', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'productinfo',
            },
        ),
    ]
