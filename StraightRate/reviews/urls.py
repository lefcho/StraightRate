from django.urls import path, include
from StraightRate.reviews import views

urlpatterns = (
    path('', views.home, name='home'),
)