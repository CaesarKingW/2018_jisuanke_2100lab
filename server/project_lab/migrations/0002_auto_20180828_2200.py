# Generated by Django 2.1 on 2018-08-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='distory_time',
            field=models.FloatField(blank=True, null=True, verbose_name='可阅时长'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='start_time',
            field=models.BigIntegerField(default=0, verbose_name='开始学习时间'),
        ),
    ]
