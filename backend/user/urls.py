from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/', views.get_users, name='users'),
    path('users/profile/', views.get_user_profile, name='users-profile'),
    path('users/profile/update/', views.update_user_profile, name='update_users-profile'),
    path('users/register/', views.register_user, name='register'),
]
