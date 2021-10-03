from rest_framework import viewsets
from accounts.models import AccountVendor
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.vendor_serializers import AccountVendorSerializer
from accounts.paginations.paginations import CustomPageNumberPagination


class AccountVendorViewSet(viewsets.ModelViewSet):
    queryset = AccountVendor.objects.all()
    serializer_class = AccountVendorSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

