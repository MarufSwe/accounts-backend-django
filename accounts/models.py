from django.db import models


# Vendor Model
class AccountVendor(models.Model):
    class State(models.TextChoices):
        Dhaka = 'dhaka', ('Dhaka')
        Chattogram = 'chattogram', ('Chattogram')
        Rajshahi = 'rajshahi', ('Rajshahi')
        Barishal = 'barishal', ('Barishal')
        Khulna = 'khulna', ('Khulna')
        Rangpur = 'rangpur', ('Rangpur')
        Mymensingh = 'mymensingh', ('Mymensingh')
        Sylhet = 'sylhet', ('Sylhet')

    vendor_name = models.CharField(max_length=30, null=False, blank=False)
    vendor_id = models.CharField(max_length=20, unique=True, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True, choices=State.choices, default=State.Dhaka)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    license_no = models.CharField(max_length=50, blank=True, null=True)
    seller_permit = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    point_of_contact = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    credit_allowance = models.CharField(max_length=6, null=True, blank=True)
    collection = models.BooleanField(default=True, blank=True, null=True)
    outstanding_credit = models.CharField(max_length=100, null=True, blank=True)
    last_order = models.DateField(editable=True, blank=True, null=True)

    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.vendor_name


class ScheduleEducation(models.Model):
    acc_vendor = models.ForeignKey(AccountVendor, on_delete=models.SET_NULL, null=True, related_name='vendor_education')
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.DateField(editable=True, blank=True, null=True)
    no_of_hours = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)

    def __str__(self):
        return self.name


class CreateReport(models.Model):
    acc_vendor = models.ForeignKey(AccountVendor, on_delete=models.SET_NULL, null=True,
                                   related_name='vendor_create_report')
    brand = models.CharField(max_length=100, blank=True, null=True)
    product_location = models.TextField(blank=True, null=True)
    brand_exposure = models.BooleanField(default=True, blank=True, null=True)
    product_visibility = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.brand


class CreateMerchandise(models.Model):
    product = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    # image = models.ImageField(upload_to='images', verbose_name='Product Image', null=True, blank=True)

    def __str__(self):
        return self.product

    # def image_img(self):
    #     if self.image:
    #         return u'<img src="%s" width="50" height="50" />' % self.image.url
    #     else:
    #         return '(Sin imagen)'
    #
    # image_img.short_description = 'Thumb'
    # image_img.allow_tags = True


class OrderMerchandise(models.Model):
    class DeliveryTime(models.TextChoices):
        Morning = 'morning', ('Morning')
        Afternoon = 'afternoon', ('Afternoon')

    # acc_vendor = models.ForeignKey(AccountVendor, on_delete=models.SET_NULL, null=True,
    #                                related_name='vendor_order_merchandise')
    # create_merchandise = models.ForeignKey(CreateMerchandise, on_delete=models.SET_NULL, null=True,
    #                                        related_name='cmerchandise_order_merchandise')

    acc_vendor = models.ForeignKey(AccountVendor, on_delete=models.SET_NULL, null=True, related_name='om_av')
    cm = models.ForeignKey(CreateMerchandise, on_delete=models.SET_NULL, null=True, related_name='om_cm')

    quantity = models.IntegerField(blank=True, null=True)
    delivery_date = models.DateField(editable=True, blank=True, null=True)
    delivery_time = models.CharField(max_length=20, blank=True, null=True, choices=DeliveryTime.choices,
                                     default=DeliveryTime.Morning)


class CustomInfo(models.Model):
    license = models.CharField(max_length=200, blank=True, null=True)
    product_type = models.CharField(max_length=200, blank=True, null=True)
    flower_type = models.CharField(max_length=200, blank=True, null=True)
    grow_method = models.CharField(max_length=200, blank=True, null=True)
    nutrients_used = models.TextField(blank=True, null=True)
    trim_method = models.CharField(max_length=200, blank=True, null=True)
    curing_time = models.CharField(max_length=200, blank=True, null=True)
    growing_location = models.CharField(max_length=200, blank=True, null=True)
    brand_headquarters = models.CharField(max_length=200, blank=True, null=True)
    website_url = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    point_of_contact = models.CharField(max_length=200, blank=True, null=True)
    brand_history_and_mission = models.CharField(max_length=200, blank=True, null=True)
    flower_quality = models.CharField(max_length=200, blank=True, null=True)
    price_point = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


class MediaLibrary(models.Model):
    image_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)


