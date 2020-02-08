from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='user_login'),
    path('', include(router.urls)),
]
