from django.db import models
from .fields import ColorField

# Create your models here.

class Teachers(models.Model):
    short_name = models.CharField("Имя", max_length=255)
    name = models.CharField("ФИО", max_length=255)
    position = models.CharField("Должность", max_length=255)
    qimage = models.ImageField('Фото',default = '1.jpg', blank = True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'

class Places(models.Model):
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'


class Appointments(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField('Описание')
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    start_time = models.TimeField('Время начала')
    end_time = models.TimeField('Время окончания')
    appointment_id = models.CharField("ID Мероприятия", max_length=255, blank=True)
    service_id = models.CharField("ID Услуги", max_length=255,
                                  default='3474cd5c-6f7c-11e8-814e-9c5c8e747603')
    pay = models.BooleanField('Оплачено', default=False)
    appointment = models.BooleanField('Назначено', default=False)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE,
                                verbose_name='Учитель')
    color = ColorField('Цвет', default='#FF0000')
    availability = models.SmallIntegerField('Доступность')
    weekDay = models.SmallIntegerField('День недели', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
