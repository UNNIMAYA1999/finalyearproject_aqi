# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import aerifyDailyAPIViewSet, aerifyMonthlyAPIViewSet, aerifyYearlyAPIViewSet


router = DefaultRouter()

router.register(r'api-daily', aerifyDailyAPIViewSet),
router.register(r'api-monthly', aerifyMonthlyAPIViewSet),
router.register(r'api-yearly', aerifyYearlyAPIViewSet),
# router.register(r'api_city', aerifyCityAPIViewSet),

urlpatterns = router.urls
