from django.urls import path, include
from accounts.views.vendor_views import AccountVendorViewSet
from accounts.views.shcedule_education_views import ScheduleEducationViewSet
from accounts.views.create_report_views import CreateReportViewSet
from accounts.views.merchandise_views import MerchandiseViewSet
from accounts.views.order_merchan_views import OrderMerchandiseViewSet
from accounts.views.custome_info_views import CustomInfoViewSet
from accounts.views.register_views import RegisterAPI
from accounts.views.login_views import LoginAPI
from accounts.views.media_library_views import MediaLibraryViewSet
from knox import views as knox_views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('acc-vendor', AccountVendorViewSet)
router.register('education', ScheduleEducationViewSet)
router.register('create-report', CreateReportViewSet)
router.register('merchandise', MerchandiseViewSet)
router.register('order-merchandise', OrderMerchandiseViewSet)
router.register('custom-info', CustomInfoViewSet)
router.register('media-library', MediaLibraryViewSet)
# router.register('register', RegisterAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('acc-vendor/', views.vendor_views.AccountVendorViewSet),
    path('education/', views.shcedule_education_views.ScheduleEducationViewSet),
    path('create-report/', views.create_report_views.CreateReportViewSet),
    path('merchandise/', views.merchandise_views.MerchandiseViewSet),
    path('order-merchandise/', views.order_merchan_views.OrderMerchandiseViewSet),
    path('custom-info/', views.custome_info_views.CustomInfoViewSet),
    path('media-library/', views.media_library_views.MediaLibraryViewSet),

    # path('register/', views.register_views.RegisterAPI),
    path('register/', RegisterAPI.as_view()),

    path('login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
]

