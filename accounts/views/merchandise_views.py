from rest_framework import viewsets
from accounts.models import CreateMerchandise
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.merchandiser_serializers import MerchandiseSerializer
from accounts.paginations.paginations import CustomPageNumberPagination


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchandise.objects.all()
    serializer_class = MerchandiseSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

