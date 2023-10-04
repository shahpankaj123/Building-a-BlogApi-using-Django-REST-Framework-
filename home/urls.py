from django.urls import path
from home import views

urlpatterns = [
    
    path('api/',views.home.as_view()),

]    