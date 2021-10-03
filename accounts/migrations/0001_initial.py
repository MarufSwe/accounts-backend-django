# Generated by Django 3.1.2 on 2021-10-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=30)),
                ('vendor_id', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, choices=[('dhaka', 'Dhaka'), ('chattogram', 'Chattogram'), ('rajshahi', 'Rajshahi'), ('barishal', 'Barishal'), ('khulna', 'Khulna'), ('rangpur', 'Rangpur'), ('mymensingh', 'Mymensingh'), ('sylhet', 'Sylhet')], default='dhaka', max_length=20, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('license_no', models.CharField(blank=True, max_length=50, null=True)),
                ('seller_permit', models.CharField(blank=True, max_length=15, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=30, null=True)),
                ('point_of_contact', models.CharField(blank=True, max_length=30, null=True)),
                ('instagram', models.CharField(blank=True, max_length=30, null=True)),
                ('credit_allowance', models.CharField(blank=True, max_length=6, null=True)),
                ('collection', models.BooleanField(blank=True, default=True, null=True)),
                ('outstanding_credit', models.CharField(blank=True, max_length=100, null=True)),
                ('last_order', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='CreateMerchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(blank=True, max_length=200, null=True)),
                ('product_type', models.CharField(blank=True, max_length=200, null=True)),
                ('flower_type', models.CharField(blank=True, max_length=200, null=True)),
                ('grow_method', models.CharField(blank=True, max_length=200, null=True)),
                ('nutrients_used', models.TextField(blank=True, null=True)),
                ('trim_method', models.CharField(blank=True, max_length=200, null=True)),
                ('curing_time', models.CharField(blank=True, max_length=200, null=True)),
                ('growing_location', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_headquarters', models.CharField(blank=True, max_length=200, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('point_of_contact', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_history_and_mission', models.CharField(blank=True, max_length=200, null=True)),
                ('flower_quality', models.CharField(blank=True, max_length=200, null=True)),
                ('price_point', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('date_time', models.DateField(blank=True, null=True)),
                ('no_of_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('acc_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_education', to='accounts.accountvendor')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMerchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('delivery_time', models.CharField(blank=True, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon')], default='morning', max_length=20, null=True)),
                ('acc_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='om_av', to='accounts.accountvendor')),
                ('cm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='om_cm', to='accounts.createmerchandise')),
            ],
        ),
        migrations.CreateModel(
            name='CreateReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('product_location', models.TextField(blank=True, null=True)),
                ('brand_exposure', models.BooleanField(blank=True, default=True, null=True)),
                ('product_visibility', models.BooleanField(blank=True, default=True, null=True)),
                ('acc_vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_create_report', to='accounts.accountvendor')),
            ],
        ),
    ]