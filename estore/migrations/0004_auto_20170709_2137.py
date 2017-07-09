# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estore', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_name', models.CharField(max_length=255, verbose_name='付款人姓名')),
                ('billing_address', models.CharField(max_length=255, verbose_name='帳單地址')),
                ('shipping_name', models.CharField(max_length=255, verbose_name='收件人姓名')),
                ('shipping_address', models.CharField(max_length=255, verbose_name='收件地址')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='產品名稱')),
                ('price', models.CharField(max_length=255, verbose_name='價格')),
                ('quantity', models.CharField(max_length=255, verbose_name='數量')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='estore.OrderInfo')),
                ('total', models.IntegerField(default=0, verbose_name='訂單總金額')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estore.Order'),
        ),
    ]
