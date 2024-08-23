from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect

from StraightRate.reviews.forms import AddMovieReviewForm, AddVideoGameReviewForm, EditMovieReviewForm, \
    EditVideoGameReviewForm
from StraightRate.reviews.models import Movie, VideoGame, MovieReview


def home(request):
    top_movies = (Movie.objects
                  .annotate(avg_rating=Avg('reviews__rating'),
                            review_count=Count('reviews'))
                  .filter(review_count__gt=0)
                  .order_by('-avg_rating')
    [:5])
    top_games = (VideoGame.objects
                 .annotate(avg_rating=Avg('reviews__rating'),
                           review_count=Count('reviews'))
                 .filter(review_count__gt=0)
                 .order_by('-avg_rating')
    [:5])
    context = {
        'top_movies': top_movies,
        'top_games': top_games,
    }

    return render(request, 'common/home.html', context)


def details_movie_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()
    user_review = MovieReview.objects.filter(movie=movie, user=request.user).first()

    if request.method == 'POST':
        if 'delete_review' in request.POST:
            # Handle delete review
            review_id = request.POST.get('review_id')
            review = get_object_or_404(MovieReview, id=review_id, user=request.user)
            review.delete()
            messages.success(request, "Your review has been deleted successfully.")
            return redirect('details-movie', movie_id=movie_id)

        else:
            # Handle save review
            form = AddMovieReviewForm(request.POST, instance=user_review)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                messages.success(request, "Your review has been saved successfully.")
                return redirect('details-movie', movie_id=movie_id)
            else:
                messages.error(request, "There was a problem saving your review.")
    else:
        form = AddMovieReviewForm(instance=user_review)

    context = {
        'movie': movie,
        'reviews': reviews,
        'user_review': user_review,
        'form': form,
    }
    return render(request, 'movies/movie-details.html', context)


@login_required
def delete_review(request, review_id):
    # Get the review object, or return a 404 if it doesn't exist
    review = get_object_or_404(MovieReview, id=review_id)

    # Check if the user is the owner of the review
    if review.user == request.user:
        # Delete the review
        review.delete()
        messages.success(request, "Your review has been deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this review.")

    # Redirect to the movie details page (or any other relevant page)
    return redirect('details-movie', movie_id=review.movie.id)


def details_game_view(request, game_id):
    video_game = get_object_or_404(VideoGame, id=game_id)
    reviews = video_game.reviews.all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = AddVideoGameReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.video_game = video_game
            review.user = request.user
            review.save()
            return redirect('details-video-game', game_id=game_id)
    else:
        form = AddVideoGameReviewForm()

    context = {
        'video_game': video_game,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'video-games/video-games-details.html', context)


def movie_dashboard(request):
    genres = Movie.MovieGenreChoices.choices
    movies_by_genre = {genre[1]: Movie.objects.filter(genre=genre[0]) for genre in genres}

    context = {
        'movies_by_genre': movies_by_genre,
    }
    return render(request, 'movies/movies-dashboard.html', context)


def video_games_dashboard(request):
    genres = VideoGame.VideoGameGenreChoices.choices
    games_by_genre = {genre[1]: VideoGame.objects.filter(genre=genre[0]) for genre in genres}

    context = {
        'games_by_genre': games_by_genre,
    }
    return render(request, 'video-games/video-games-dashboard.html', context)
