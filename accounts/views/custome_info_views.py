from rest_framework import viewsets
from accounts.models import CustomInfo
from accounts.serializers.custom_info_serializers import CustomInfoListSerializer


class CustomInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomInfo.objects.all()
    serializer_class = CustomInfoListSerializer

