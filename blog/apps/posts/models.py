from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User
from apps.categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(
        upload_to="posts/images/"
    )  # definimos la ruta en donde se va a guardar la imagen
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=SET_NULL, null=True
    )  # con esto le asociamos un usuario y en caso de eliminar se colocará en null
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
