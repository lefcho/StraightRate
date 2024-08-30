from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect

from StraightRate.reviews.forms import AddMovieReviewForm, AddVideoGameReviewForm, SearchForm
from StraightRate.reviews.models import Movie, VideoGame, MovieReview, VideoGameReview


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
                review.rating = request.POST.get('rating')
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


@login_required
def details_game_view(request, game_id):
    # Fetch the video game by its ID
    video_game = get_object_or_404(VideoGame, id=game_id)

    # Get all reviews for the video game
    reviews = video_game.reviews.all()

    # Fetch the user's existing review if it exists
    user_review = VideoGameReview.objects.filter(video_game=video_game, user=request.user).first()

    if request.method == 'POST':
        if 'delete_review' in request.POST:
            # Handle deleting the review
            review_id = request.POST.get('review_id')
            review = get_object_or_404(VideoGameReview, id=review_id, user=request.user)
            review.delete()
            messages.success(request, "Your review has been deleted successfully.")
            return redirect('details-video-game', game_id=game_id)

        else:
            # Handle saving or updating the review
            form = AddVideoGameReviewForm(request.POST, instance=user_review)
            if form.is_valid():
                review = form.save(commit=False)
                review.video_game = video_game
                review.user = request.user
                review.save()
                messages.success(request, "Your review has been saved successfully.")
                return redirect('details-video-game', game_id=game_id)
            else:
                messages.error(request, "There was a problem saving your review.")
    else:
        # Load the form with the existing review if there is one
        form = AddVideoGameReviewForm(instance=user_review)

    context = {
        'video_game': video_game,
        'reviews': reviews,
        'user_review': user_review,  # Pass the user's existing review to the template
        'form': form,  # Pass the form to the template
    }

    # Render the template with the context
    return render(request, 'video-games/video-games-details.html', context)


@login_required
def delete_video_game_review(request, review_id):
    # Get the review object, or return a 404 if it doesn't exist
    review = get_object_or_404(VideoGameReview, id=review_id)

    # Check if the user is the owner of the review
    if review.user == request.user:
        # Delete the review
        review.delete()
        messages.success(request, "Your review has been deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this review.")

    # Redirect to the video game details page (or any other relevant page)
    return redirect('details-video-game', game_id=review.video_game.id)


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


def searched_media(request):
    query = request.GET.get('q')

    if len(query) == 1:
        movie_results = Movie.objects.filter(title__istartswith=query)
        game_results = VideoGame.objects.filter(title__istartswith=query)
    else:
        movie_results = Movie.objects.filter(title__icontains=query)
        game_results = VideoGame.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'movie_results': movie_results,
        'game_results': game_results,
    }
    return render(request, 'common/search.html', context)