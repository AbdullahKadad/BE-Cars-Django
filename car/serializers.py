from rest_framework import serializers
from .models import Car
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'owner']
        read_only_fields = ['owner']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        
        return data
