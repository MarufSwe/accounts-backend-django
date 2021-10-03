from rest_framework import viewsets, status
from accounts.models import CreateReport
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.create_report_serializers import CreateReportSerializer, ReportListSerializer, \
    ReportUpdateSerializer
from accounts.paginations.paginations import CustomPageNumberPagination
from django.db import transaction


class CreateReportViewSet(viewsets.ModelViewSet):
    queryset = CreateReport.objects.all()
    serializer_class = ReportListSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = CreateReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ReportUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
