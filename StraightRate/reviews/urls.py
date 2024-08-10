from django.urls import path, include
from StraightRate.reviews import views

urlpatterns = (
    path('', views.home, name='home'),
    path('<int:movie_id>/details-movie/', views.details_movie_view, name='details-movie')
)

