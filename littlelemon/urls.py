from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu-items')
router.register(r'bookings', views.BookingViewSet, basename='bookings')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),  # User registration and management
    path('auth/', include('djoser.urls.jwt')),  # JWT token authentication (optional)
    path('auth/token/login/', obtain_auth_token),
    path('api/menu/', views.MenuViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/booking/', include(router.urls)),
    path('api/', include(router.urls)),
]