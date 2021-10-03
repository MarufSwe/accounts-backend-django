from rest_framework import serializers
from accounts.models import CreateMerchandise
from django import forms


# Designation serializers
class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateMerchandise
        fields = '__all__'
        # fields = ('id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
        #             'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
        #             'credit_allowance', 'collection', 'outstanding_credit', 'last_order')

        # def get_image(self, create_merchandise):
        #     request = self.context.get('request')
        #     image_url = None
        #     if create_merchandise.image.url:
        #         image_url = create_merchandise.image.url
        #         return request.build_absolute_uri(image_url)
        #     return None
