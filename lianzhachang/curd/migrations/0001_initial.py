# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='职称')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='作业区名称')),
                ('area', models.CharField(max_length=32, verbose_name='区域')),
                ('dangerous_level', models.IntegerField(blank=True, choices=[(1, '高危'), (2, '危险'), (3, '小心'), (4, '安全')], null=True, verbose_name='危险等级')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='职位')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='工种名称')),
                ('retirement_age', models.IntegerField(verbose_name='退休年龄')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.IntegerField(unique=True, verbose_name='工号')),
                ('name', models.CharField(max_length=16, verbose_name='员工姓名')),
                ('age', models.IntegerField(blank=True, verbose_name='年龄')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=64, verbose_name='邮箱')),
                ('education', models.IntegerField(blank=True, choices=[(1, '重点大学'), (2, '普通本科'), (3, '独立院校'), (4, '民办本科'), (5, '大专'), (6, '民办专科'), (7, '高中'), (8, '其他')], null=True, verbose_name='学历')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.JobTitle')),
                ('operating_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.OperatingArea')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.Position')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curd.Profession')),
            ],
        ),
    ]
