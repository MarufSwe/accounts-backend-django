from rest_framework import serializers
from accounts.models import AccountVendor
from accounts.serializers.Base64ImageField import Base64ImageField
from django import forms


# Designation serializers
class AccountVendorSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True,)
    class Meta:
        model = AccountVendor
        fields = '__all__'
        # fields = ('id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
        #             'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
        #             'credit_allowance', 'collection', 'outstanding_credit', 'last_order')
