from django.urls import path

from rest_framework.routers import DefaultRouter

from cats import views

router = DefaultRouter()
router.register(r'cats', views.CatView, basename='cat')

urlpatterns = router.urls
