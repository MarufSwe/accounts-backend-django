from rest_framework import serializers
from accounts.models import CreateReport, AccountVendor
from django import forms


# Designation serializers
class VendorSerializerForReportList(serializers.ModelSerializer):
    class Meta:
        model = AccountVendor
        fields = ('id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
                  'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                  'credit_allowance', 'collection', 'outstanding_credit', 'last_order')


# Schedule Education serializers
class ReportListSerializer(serializers.ModelSerializer):
    acc_vendor = VendorSerializerForReportList(read_only=True)
    class Meta:
        model = CreateReport
        fields = ('id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor',)


# Schedule Education serializers
class CreateReportSerializer(serializers.ModelSerializer):
    # acc_vendor = AccountVendorSerializerForCreateReport(read_only=True)
    class Meta:
        model = CreateReport
        fields = ('id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor',)



# Schedule Education serializers
class ReportUpdateSerializer(serializers.ModelSerializer):
    # acc_vendor = AccountVendorSerializerForCreateReport(read_only=True)
    class Meta:
        model = CreateReport
        fields = ('id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor',)
