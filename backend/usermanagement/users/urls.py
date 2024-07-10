from django.urls import path
from .views import UserRegistrationView, UserDetailView, AdminLoginAPIView, UserListView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('admin/login/', AdminLoginAPIView.as_view(), name='adminlogin'),
    path('admin/users/', UserListView.as_view(), name='admin-users'),
    path('admin/users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='admin-user-update'),
]   