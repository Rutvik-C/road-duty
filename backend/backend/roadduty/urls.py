from django.urls import include, path
from rest_framework import routers

from django.urls import path, include

from .views import *
router = routers.DefaultRouter()

router.register(r'rider', RiderViewSet)
router.register(r'query', QueryViewSet)
router.register(r'challan', ChallanViewSet)
router.register(r'challan_image', ChallanImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
