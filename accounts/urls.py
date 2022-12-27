from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView

from accounts.views import LoginView, RegisterView, ChangePasswordView, UpdateProfileView

router = routers.DefaultRouter()

urlpatterns = [
	path('login/', LoginView.as_view(), name='auth_login'),
	path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
	path('logout/', TokenBlacklistView.as_view(), name='auth_logout'),
	path('register/', RegisterView.as_view(), name='auth_register'),
	path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
	path('update_account/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),

	path('', include(router.urls)),
]
