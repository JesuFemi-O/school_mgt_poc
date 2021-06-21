from django.urls import path

from .views import RegisterView, ChangePasswordView, MyTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('update_my_password/', ChangePasswordView.as_view(),
         name='update_my_password')
]
