from rest_framework.viewsets import ModelViewSet
from apps.categories.models import Category
from apps.categories.api.serializers import CategorySerializer
from apps.categories.api.permissions import IsAdminOrReadOnly

# esto me permite filtrar or campos
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  # trae todos los elementos
    # queryset = Category.objects.filter(published=True)  # trae solo las categorias publicadas
    lookup_field = (
        "slug"  # con esto me permite buscar en ligar de por el ID por el slug
    )
    # para aplciar filtros
    # paara ejecutarlo desde el front tenemos http://127.0.0.1:8000/api/categories/?published=true # el valor de published puede ser cualquiera
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["published", "title"]
