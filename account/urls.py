from django.urls import path,include
from account import views

urlpatterns = [
    path('Register/',views.RegisterView.as_view()),
    path('Login/',views.Loginview.as_view()),
]