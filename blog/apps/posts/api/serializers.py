from rest_framework import serializers
from apps.posts.models import Post

# para traert la información de las claves que tienen la clave foranea tenemos lo  importar el respectivo serialzidor
from apps.users.api.serializars import UserSerializer
from apps.categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "miniature",
            "created_at",
            "published",
            "user",
            "category",
        ]
