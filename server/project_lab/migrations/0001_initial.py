# Generated by Django 2.1 on 2018-08-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('username', models.CharField(max_length=15)),
                ('head_protrait', models.ImageField(upload_to=None)),
                ('welfare', models.FloatField(default=0)),
                ('Is_comment', models.BooleanField(default=True)),
                ('Is_teacher', models.BooleanField(default=False)),
            ],
        ),
    ]
