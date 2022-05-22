from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('msg-view', msgViewset, basename="msg-view")
router.register('msg-view-set', messageviewSet, basename="msg-view-set")

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

]
