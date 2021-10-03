from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Vendor
@admin.register(AccountVendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
                    'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                    'credit_allowance', 'collection', 'outstanding_credit', 'last_order', 'image']


@admin.register(ScheduleEducation)
class ScheduleEducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'email', 'brand', 'date_time', 'no_of_hours']


@admin.register(CreateReport)
class CreateReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor', ]


@admin.register(CreateMerchandise)
class CreateMerchandiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'brand', 'type', 'description', 'quantity']


@admin.register(OrderMerchandise)
class OrderMerchandiseAdmin(admin.ModelAdmin):
    # list_display = ['id', 'acc_vendor', 'create_merchandise', 'quantity', 'delivery_date', 'delivery_time',]
    list_display = ['id', 'quantity', 'delivery_date', 'delivery_time', 'acc_vendor', 'cm']


@admin.register(CustomInfo)
class CustomInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'license', 'product_type', 'flower_type', 'grow_method', 'nutrients_used', 'trim_method',
                    'curing_time', 'growing_location', 'brand_headquarters', 'website_url', 'instagram',
                    'point_of_contact', 'brand_history_and_mission', 'flower_quality', 'price_point', 'notes']


# User
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']



@admin.register(MediaLibrary)
class MediaLibraryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_name', 'image',]