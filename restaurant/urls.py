from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from .views import MenuItemViewSet, BookingViewSet, SingleMenuItemViewSet
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu-items')
router.register(r'menu/<int:pk>', SingleMenuItemViewSet, basename='single-menu-item')
router.register(r'bookings', BookingViewSet, basename='bookings')
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/menu/', views.MenuItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('menu/<int:pk>/', views.SingleMenuItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token),
]