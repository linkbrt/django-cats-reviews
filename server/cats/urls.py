from django.urls import path

from rest_framework.routers import DefaultRouter

from cats import views

router = DefaultRouter()
router.register(r'cats', views.CatView, basename='cat')
router.register(r'reviews', views.ReviewView, basename='review')

urlpatterns = router.urls
