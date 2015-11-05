# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=255, verbose_name='\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c: ')),
            ],
            options={
                'verbose_name': '\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='ControlCashMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factory_number', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440', blank=True)),
                ('inventory_number', models.CharField(max_length=255, null=True, verbose_name='\u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u041a\u041c',
                'verbose_name_plural': '\u041a\u041a\u041c',
            },
        ),
        migrations.CreateModel(
            name='DeregistrationDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deregistration_date', models.DateField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043d\u044f\u0442\u0438\u044f \u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0434\u0430\u0442\u0430 \u0441\u043d\u044f\u0442\u0438\u044f \u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0434\u0430\u0442\u044b \u0441\u043d\u044f\u0442\u0438\u0439 \u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factory_number', models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440', blank=True)),
                ('inventory_number', models.CharField(max_length=255, null=True, verbose_name='\u0438\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440', blank=True)),
            ],
            options={
                'verbose_name': '\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u0434\u0440\u0443\u0433\u0438\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430',
            },
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435/\u043c\u043e\u0434\u0435\u043b\u044c', blank=True)),
                ('brand', models.ForeignKey(verbose_name='\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c', blank=True, to='base.Brand', null=True)),
            ],
            options={
                'verbose_name': '\u0432\u0438\u0434 \u0442\u0435\u0445\u043d\u0438\u043a\u0438',
                'verbose_name_plural': '\u0432\u0438\u0434\u044b \u0442\u0435\u0445\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ', blank=True)),
                ('address', models.CharField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441: ', blank=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: ', blank=True)),
                ('work_hours', models.CharField(max_length=255, null=True, verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b: ', blank=True)),
                ('number', models.CharField(unique=True, max_length=8, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u043d\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0439 \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u0438')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u0430\u044f \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u044b\u0435 \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Phonenumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(unique=True, max_length=255, verbose_name='\u043d\u043e\u043c\u0435\u0440')),
                ('details', models.CharField(max_length=255, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('inspection', models.ForeignKey(verbose_name='\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u0430\u044f \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f', blank=True, to='base.Inspection', null=True)),
            ],
            options={
                'verbose_name': '\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440',
                'verbose_name_plural': '\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0435 \u043d\u043e\u043c\u0435\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_number', models.CharField(max_length=10, null=True, verbose_name='\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440', blank=True)),
                ('registration_date', models.DateField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True)),
                ('deregistration_date', models.DateField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043d\u044f\u0442\u0438\u044f \u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True)),
                ('control_cash_machine', models.ForeignKey(verbose_name='\u041a\u041a\u041c', blank=True, to='base.ControlCashMachine', null=True)),
            ],
            options={
                'verbose_name': '\u0441\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f\u0445',
            },
        ),
        migrations.CreateModel(
            name='RegistrationDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_date', models.DateField(null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0434\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0434\u0430\u0442\u044b \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Serviced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: ', blank=True)),
                ('address', models.CharField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441: ', blank=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: ', blank=True)),
                ('work_hours', models.CharField(max_length=255, null=True, verbose_name='\u0447\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b: ', blank=True)),
                ('inn', models.CharField(max_length=12, verbose_name='\u0418\u041d\u041d', blank=True)),
                ('inspection', models.ForeignKey(verbose_name='\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u0430\u044f \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f', blank=True, to='base.Inspection', null=True)),
            ],
            options={
                'verbose_name': '\u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u0430\u044f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=255, verbose_name='\u0432\u0435\u0440\u0441\u0438\u044f: ')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: ', blank=True)),
            ],
            options={
                'verbose_name': '\u0432\u0435\u0440\u0441\u0438\u044f',
                'verbose_name_plural': '\u0432\u0435\u0440\u0441\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('status', models.CharField(max_length=255, null=True, verbose_name='\u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True)),
                ('workplace', models.ForeignKey(verbose_name='\u043c\u0435\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u044b', blank=True, to='base.Serviced', null=True)),
            ],
            options={
                'ordering': ('workplace',),
                'verbose_name': '\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a',
                'verbose_name_plural': '\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='organization',
            field=models.ForeignKey(verbose_name='\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', blank=True, to='base.Serviced', null=True),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='worker',
            field=models.ForeignKey(verbose_name='\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a', blank=True, to='base.Worker', null=True),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='version',
            field=models.ForeignKey(verbose_name='\u0432\u0435\u0440\u0441\u0438\u044f', blank=True, to='base.Version', null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c', blank=True, to='base.DeviceModel', null=True),
        ),
        migrations.AddField(
            model_name='controlcashmachine',
            name='device_model',
            field=models.ForeignKey(verbose_name='\u043c\u043e\u0434\u0435\u043b\u044c', blank=True, to='base.DeviceModel', null=True),
        ),
        migrations.AddField(
            model_name='controlcashmachine',
            name='inspection',
            field=models.ForeignKey(verbose_name='\u043d\u0430\u043b\u043e\u0433\u043e\u0432\u0430\u044f \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f', blank=True, to='base.Inspection', null=True),
        ),
        migrations.AddField(
            model_name='controlcashmachine',
            name='registration_data',
            field=models.ForeignKey(verbose_name='\u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True, to='base.RegistrationData', null=True),
        ),
        migrations.AddField(
            model_name='controlcashmachine',
            name='serviced',
            field=models.ForeignKey(verbose_name='\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', blank=True, to='base.Serviced', null=True),
        ),
    ]
