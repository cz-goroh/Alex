from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appointments, Teachers
from .serializers import AppointmentsSerializer, TeachersSerialiser, AppSer


class AppointmentsView(APIView):
    def get(self, request):
        appointments = Appointments.objects.all()
        serializer = AppointmentsSerializer(appointments, many=True)
        return Response(serializer.data)
