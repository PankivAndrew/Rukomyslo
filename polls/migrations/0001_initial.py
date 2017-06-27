# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('CategoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerID', models.IntegerField(primary_key=True, serialize=False)),
                ('PhoneNumber', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('MaterialsID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocalID', models.IntegerField()),
                ('MaterialsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Materials')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.IntegerField(primary_key=True, serialize=False)),
                ('OrderTotalPrice', models.DecimalField(decimal_places=5, max_digits=10)),
                ('OrderDate', models.DateField()),
                ('OrderDetails', models.TextField()),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Description', models.TextField()),
                ('IsDeleted', models.BinaryField()),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Description', models.TextField()),
                ('Quantity', models.IntegerField()),
                ('Address', models.CharField(max_length=200)),
                ('CategoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.IntegerField()),
                ('ContactPerson', models.CharField(max_length=100)),
                ('Phone1', models.CharField(max_length=13)),
                ('Phone2', models.CharField(max_length=13)),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageID', models.IntegerField()),
                ('NameOfImage', models.CharField(max_length=50)),
                ('ProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product')),
            ],
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='ProductID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
        ),
        migrations.AddField(
            model_name='materialsproduct',
            name='ProductID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
        ),
    ]
