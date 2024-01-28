from rest_framework.permissions import BasePermission
from apps.comments.models import Comment


class IsOwnerorReadAndCreateOnly(BasePermission):
    """
    Permite restringir la edición y eliminación de comentarios solo por el usuario dueño del comentario
    """

    def has_permission(self, request, view):
        if request.method in ["GET", "POST"]:
            return True
        else:
            id_comment = view.kwargs[
                "pk"
            ]  # obtenemos el id del comentario a eliminar o editar
            comment = Comment.objects.get(pk=id_comment)  # traemos el comentario

            id_user = (
                request.user.pk
            )  # traemos el id del usario que esta haciendo la petición
            id_user_comment = (
                comment.user_id
            )  # traemos el id del usuario que creo el comentario

            if id_user == id_user_comment:
                return True
            return False
