from rest_framework import serializers
from accounts.models import ScheduleEducation, AccountVendor
from django import forms


class AccountVendorSerializerForScheduleEducation(serializers.ModelSerializer):
    class Meta:
        model = AccountVendor
        fields = ('id', 'vendor_id', 'vendor_name')


# Schedule Education serializers
class ScheduleEducationListSerializer(serializers.ModelSerializer):
    acc_vendor = AccountVendorSerializerForScheduleEducation(read_only=True)
    class Meta:
        model = ScheduleEducation
        fields = ('id', 'name', 'address', 'phone', 'email', 'brand', 'date_time', 'no_of_hours', 'acc_vendor')


# Schedule Education serializers
class ScheduleEducationCreateSerializer(serializers.ModelSerializer):
    # acc_vendor = AccountVendorSerializerForScheduleEducation(read_only=True)
    acc_vendor = serializers.PrimaryKeyRelatedField(many=False, queryset=AccountVendor.objects.all())
    class Meta:
        model = ScheduleEducation
        fields = ('id', 'name', 'address', 'phone', 'email', 'brand', 'date_time', 'no_of_hours', 'acc_vendor')