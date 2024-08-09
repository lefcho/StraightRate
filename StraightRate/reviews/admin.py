from django.contrib import admin

from StraightRate.reviews.models import VideoGame, Movie, MovieReview, VideoGameReview, Developer, Director
from StraightRate.users.models import User


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoGameReview)
class VideoGameReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
