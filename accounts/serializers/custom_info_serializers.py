from rest_framework import serializers
from accounts.models import CustomInfo
from django import forms


# CustomInfoListSerializer
class CustomInfoListSerializer(serializers.ModelSerializer):
    product_type = serializers.JSONField()
    flower_type = serializers.JSONField()
    grow_method = serializers.JSONField()
    trim_method = serializers.JSONField()
    flower_quality = serializers.JSONField()
    price_point = serializers.JSONField()
    class Meta:
        model = CustomInfo
        fields = ('id', 'license', 'product_type', 'flower_type', 'grow_method', 'nutrients_used', 'trim_method',
                  'curing_time', 'growing_location', 'brand_headquarters', 'website_url', 'instagram',
                  'point_of_contact', 'brand_history_and_mission', 'flower_quality', 'price_point', 'notes')
