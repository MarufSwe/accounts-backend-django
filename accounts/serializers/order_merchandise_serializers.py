from rest_framework import serializers
from accounts.models import *
from django import forms


# Designation serializers
class VendorSerializerForOrderMerchandiseList(serializers.ModelSerializer):
    class Meta:
        model = AccountVendor
        fields = ('id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
                  'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                  'credit_allowance', 'collection', 'outstanding_credit', 'last_order')


# Schedule Education serializers
class CreateMerchandiseSerializerForOrderMerchandiseList(serializers.ModelSerializer):
    class Meta:
        model = CreateMerchandise
        fields = ('id', 'product', 'brand', 'type', 'description', 'quantity',)


# Schedule Education serializers
class OrderMerchandiseListSerializer(serializers.ModelSerializer):
    acc_vendor = VendorSerializerForOrderMerchandiseList(read_only=True)
    cm = CreateMerchandiseSerializerForOrderMerchandiseList(read_only=True)
    class Meta:
        model = OrderMerchandise
        fields = ('id', 'quantity', 'delivery_date', 'delivery_time', 'acc_vendor', 'cm')



# Schedule Education serializers
class OrderMerchandiseCreateSerializer(serializers.ModelSerializer):
    acc_vendor = serializers.PrimaryKeyRelatedField(many=False, queryset=AccountVendor.objects.all())
    cm = serializers.PrimaryKeyRelatedField(many=False, queryset=CreateMerchandise.objects.all())
    class Meta:
        model = OrderMerchandise
        fields = ('id', 'acc_vendor', 'cm', 'quantity', 'delivery_date', 'delivery_time',)


#
# # Schedule Education serializers
# class ReportUpdateSerializer(serializers.ModelSerializer):
#     # acc_vendor = AccountVendorSerializerForCreateReport(read_only=True)
#     class Meta:
#         model = CreateReport
#         fields = ('id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor',)
