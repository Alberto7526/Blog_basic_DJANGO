from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.api.serializars import (
    UserRegisterSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class RegisterView(APIView):
    """
    Esta vista me permite gestionar todo el CRUD de usuarios
    """

    def post(self, request):
        """
        Documentación para el metodo post...
        """
        serializer = UserRegisterSerializer(
            data=request.data
        )  # obtenemos los datos del request y los serializamos
        if serializer.is_valid(
            raise_exception=True
        ):  # validamos los datos, si es correcto entra, sino casa una excepción
            serializer.save()  # guarmamos el dato
            return Response(
                serializer.data
            )  # respondemos con el mismo dato en caso correcto
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # respondemos un bad request y el error


class UserView(APIView):
    """
    Permite devolver la información del usuario, sin la contraseña, solo si ya se encuentra autenticado
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Usando el nuevo serializador devolvemos los datos del usuario
        se requiere enviar el token de autenticación en los headers precedido de la palabra Bearer

        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        """
        Utilizado para actualizar los datos del usuario, se utiliza un serialziador diferente para controlar que datos
        puede actualizar
        """
        user = User.objects.get(
            id=request.user.id
        )  # obtenemos los datos del usuario que hace la petición
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
