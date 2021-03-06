from django.contrib import admin
from django.urls import path, include
from API import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('User', views.UserviewSet, basename='username')
router.register('Cab', views.CarviewSet, basename='modl')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
