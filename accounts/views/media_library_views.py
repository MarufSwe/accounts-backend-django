from rest_framework import viewsets
from accounts.models import MediaLibrary
from accounts.serializers.media_library_serializers import MediaLibrarySerializer


class MediaLibraryViewSet(viewsets.ModelViewSet):
    queryset = MediaLibrary.objects.all()
    serializer_class = MediaLibrarySerializer


