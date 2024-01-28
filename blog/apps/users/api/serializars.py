from rest_framework import serializers
from apps.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Define los campos a utilizar por el serialziador
        """

        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        """
        Sobre escribimos este metodo para encriptar la contraseña, esto lo hce Django por debajo, pero se debe indicarle que lo haga
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
