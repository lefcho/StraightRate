from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Value, Q
from django.db.models.functions import Concat
from django.shortcuts import render, get_object_or_404, redirect

from StraightRate.reviews.forms import AddMovieReviewForm, AddVideoGameReviewForm
from StraightRate.reviews.models import Movie, VideoGame, MovieReview, VideoGameReview, Director, Developer


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
    user_review = None
    form = None

    if request.user.is_authenticated:
        user_review = MovieReview.objects.filter(movie=movie, user=request.user).first()

        if request.method == 'POST':
            if 'delete_review' in request.POST:
                review_id = request.POST.get('review_id')
                review = get_object_or_404(MovieReview, id=review_id, user=request.user)
                review.delete()
                messages.success(request, "Your review has been deleted successfully.")
                return redirect('details-movie', movie_id=movie_id)

            else:
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
    review = get_object_or_404(MovieReview, id=review_id)

    if review.user == request.user:
        review.delete()

    return redirect('details-movie', movie_id=review.movie.id)


@login_required
def details_game_view(request, game_id):
    video_game = get_object_or_404(VideoGame, id=game_id)

    reviews = video_game.reviews.all()

    user_review = VideoGameReview.objects.filter(video_game=video_game, user=request.user).first()

    if request.method == 'POST':
        if 'delete_review' in request.POST:
            review_id = request.POST.get('review_id')
            review = get_object_or_404(VideoGameReview, id=review_id, user=request.user)
            review.delete()
            messages.success(request, "Your review has been deleted successfully.")
            return redirect('details-video-game', game_id=game_id)

        else:
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
        form = AddVideoGameReviewForm(instance=user_review)

    context = {
        'video_game': video_game,
        'reviews': reviews,
        'user_review': user_review,
        'form': form,
    }

    return render(request, 'video-games/video-games-details.html', context)


@login_required
def delete_video_game_review(request, review_id):
    review = get_object_or_404(VideoGameReview, id=review_id)

    if review.user == request.user:
        review.delete()
        messages.success(request, "Your review has been deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this review.")

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

    directors = Director.objects.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    ).filter(
        Q(full_name__icontains=query)
    )

    developers = Developer.objects.filter(developer_name__icontains=query)

    if len(query) == 1:
        movie_results = Movie.objects.filter(title__istartswith=query)
        game_results = VideoGame.objects.filter(title__istartswith=query)
    else:
        movie_results = Movie.objects.filter(title__icontains=query)
        game_results = VideoGame.objects.filter(title__icontains=query)
        directors = Director.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).filter(
            Q(full_name__icontains=query)
        )

        developers = Developer.objects.filter(developer_name__icontains=query)

    context = {
        'query': query,
        'movie_results': movie_results,
        'game_results': game_results,
        'directors': directors,
        'developers': developers,
    }
    return render(request, 'common/search.html', context)


def developer_view(request, developer_id):
    developer = get_object_or_404(Developer, id=developer_id)
    games = developer.games.all()

    context = {
        'developer': developer,
        'games': games,
    }

    return render(request, 'common/developer.html', context)


def director_view(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    movies = director.movies.all()

    contex = {
        'director': director,
        'movies': movies,
    }

    return render(request, 'common/director.html', contex)
