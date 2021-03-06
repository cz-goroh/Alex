# Generated by Django 3.0.3 on 2020-03-01 08:51

import Tranings.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Студия',
                'verbose_name_plural': 'Студии',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('qimage', models.ImageField(blank=True, default='1.jpg', upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учители',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('start_time', models.TimeField(verbose_name='Время начала')),
                ('end_time', models.TimeField(verbose_name='Время окончания')),
                ('appointment_id', models.CharField(blank=True, max_length=255, verbose_name='ID Мероприятия')),
                ('service_id', models.CharField(default='3474cd5c-6f7c-11e8-814e-9c5c8e747603', max_length=255, verbose_name='ID Услуги')),
                ('pay', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('appointment', models.BooleanField(default=False, verbose_name='Назначено')),
                ('color', Tranings.fields.ColorField(default='#FF0000', max_length=7, verbose_name='Цвет')),
                ('availability', models.SmallIntegerField(verbose_name='Доступность')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tranings.Places')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tranings.Teachers', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
            },
        ),
    ]
