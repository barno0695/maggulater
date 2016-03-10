# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('maggulater', '0003_auto_20160310_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance_sheet',
            name='Marks_Obtained',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='performance_sheet',
            name='Marks_Total',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='Date_Time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 10, 7, 41, 6, 619022)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 10, 7, 41, 6, 622237)),
        ),
        migrations.AlterField(
            model_name='performance_sheet',
            name='Student_Id',
            field=models.ForeignKey(to='maggulater.Student'),
        ),
        migrations.AlterField(
            model_name='performance_sheet',
            name='Test_Id',
            field=models.ForeignKey(to='maggulater.Test'),
        ),
    ]
