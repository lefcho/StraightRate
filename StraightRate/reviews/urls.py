from django.urls import path, include
from StraightRate.reviews import views

urlpatterns = (
    path('', views.home, name='home'),
    path('<int:movie_id>/details-movie/', views.details_movie_view, name='details-movie'),
    path('<int:game_id>/details-video-game/', views.details_game_view, name='details-video-game'),
    path('movies/', views.movie_dashboard, name='movie-dashboard'),
)

