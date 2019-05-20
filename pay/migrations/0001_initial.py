# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-29 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.IntegerField(choices=[(0, '未绑定'), (1, '工商银行'), (2, '建设银行'), (3, '中信银行'), (4, '中国银行'), (5, '支付宝')], default=0, verbose_name='绑定银行')),
                ('bankid', models.CharField(max_length=13, verbose_name='银行卡号')),
                ('status', models.BooleanField(default=False, verbose_name='是否冻结')),
            ],
        ),
        migrations.CreateModel(
            name='Banklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100, verbose_name='银行')),
                ('bankimg', models.ImageField(default='logo.png', upload_to='banklist', verbose_name='logo')),
            ],
        ),
    ]
