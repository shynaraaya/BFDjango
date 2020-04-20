from rest_framework import serializers

from todo.auth_.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
