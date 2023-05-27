from rest_framework import serializers
from .models import User


class Create_User_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class Show_User_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name' , 'last_name' , 'phone']
        model = User