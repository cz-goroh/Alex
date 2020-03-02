from rest_framework import serializers
from .models import Teachers, Appointments


class TeachersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['name', 'position', 'qimage']
        view_name='track-detail'


class AppSer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'
        depth = 2


class AppointmentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')
    appointment_id = serializers.CharField(max_length=255)
    service_id = serializers.CharField(max_length=255)
    pay = serializers.BooleanField()
    appointment = serializers.BooleanField()
    color = serializers.CharField()
    availability = serializers.IntegerField()
    teacher = serializers.CharField()
    place = serializers.CharField()
    weekDay = serializers.IntegerField()

    teacher_v2 = serializers.SerializerMethodField('get_teacher')

    def get_teacher(self, obj):
        return {
            'short_name': obj.teacher.short_name,
            'name': obj.teacher.name,
            'position': obj.teacher.position,
            'imageUrl': 'http://185.144.29.172:8004' + obj.teacher.qimage.url,
        }
