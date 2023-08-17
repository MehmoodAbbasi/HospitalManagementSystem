from api_v1.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('products',ProductViewSet)