from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.comments.models import Comment
from apps.comments.api.serializers import CommentSerializer
from apps.comments.api.permissions import IsOwnerorReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerorReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # con esto podemos crear los filtros en este caso ordenar el resultado de manera descendente
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ["-created_at"]
    # Esto me permite filtrar por un campo en partocular
    filterset_fields = ["post"]
