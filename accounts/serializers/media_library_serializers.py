from rest_framework import serializers
from accounts.models import MediaLibrary
from django import forms


# Designation serializers
class MediaLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLibrary
        fields = '__all__'
        # fields = ('id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
        #             'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
        #             'credit_allowance', 'collection', 'outstanding_credit', 'last_order')
