from rest_framework import serializers
from .models import Teacher
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "number", "user"]

    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        if user:
            teacher = Teacher.objects.create(user_id=user.id, **validated_data)
            return teacher
        return None

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.email = user_data.get('email', user.email)
        user.save()

        instance.number = validated_data.get('number', instance.number)
        instance.save()

        return instance
