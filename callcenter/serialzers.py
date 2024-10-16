from rest_framework import serializers
from .models import Agent, Shift, Availability, TimeOff, ShiftSwap, ShiftLog

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'
        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'
        
        
class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
        
class TimeOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOff
        fields = '__all__'
        
class ShiftSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftSwap
        fields = '__all__'
        
class ShiftLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftLog
        fields = '__all__'