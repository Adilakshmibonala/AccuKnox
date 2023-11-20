from rest_framework import routers
from social_networking.views.user.register import RegisterUserViewSet

router = routers.DefaultRouter()
router.register(prefix=r'register', viewset=RegisterUserViewSet, basename="UserRegister")
