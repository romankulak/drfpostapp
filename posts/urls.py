from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]