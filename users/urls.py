from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginJWTView


urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/login/', LoginJWTView.as_view()),
    path('users/login/refresh/', TokenRefreshView.as_view()),
    path('users/<int:user_id>/', views.UserDetailView.as_view())
]
