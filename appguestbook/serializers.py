from rest_framework import serializers
from .models import TblEvent, TblGuest

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblEvent
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblGuest
        fields = '__all__'

