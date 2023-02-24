from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket, QrCode


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class QrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = '__all__'
