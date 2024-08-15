from django.db import models
from django.conf import settings
from django.db.models import Avg


class Review(models.Model):
    class Meta:
        abstract = True

    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        verbose_name='Rating',
    )

    comment = models.TextField(
        verbose_name='Comment',
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Director(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name='Last Name',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Developer(models.Model):
    developer_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Developer Name',
    )

    website = models.URLField(
        null=True,
        blank=True,
        verbose_name='Website',
    )

    def __str__(self):
        return self.developer_name


class Movie(models.Model):
    class MovieGenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        ADVENTURE = 'Adventure', 'Adventure'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        FANTASY = 'Fantasy', 'Fantasy'
        HORROR = 'Horror', 'Horror'
        MYSTERY = 'Mystery', 'Mystery'
        ROMANCE = 'Romance', 'Romance'
        SCI_FI = 'Sci-Fi', 'Science Fiction'
        THRILLER = 'Thriller', 'Thriller'
        WESTERN = 'Western', 'Western'
        DOCUMENTARY = 'Documentary', 'Documentary'
        ANIMATION = 'Animation', 'Animation'
        MUSICAL = 'Musical', 'Musical'
        HISTORICAL = 'Historical', 'Historical'

    title = models.CharField(
        max_length=150,
        verbose_name='Title',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    release_date = models.DateField(
        verbose_name='Release Date',
    )

    genre = models.CharField(
        max_length=100,
        choices=MovieGenreChoices.choices,
        verbose_name='Genre',
    )

    director = models.ForeignKey(
        to=Director,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movies',
        verbose_name='Director',
    )

    poster = models.ImageField(
        upload_to='posters/',
        null=True,
        blank=True,
    )

    def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 1) if avg_rating is not None else None

    def director_full_name(self):
        if self.director:
            return f"{self.director.first_name} {self.director.last_name}"
        return 'No director assigned'

    def __str__(self):
        return self.title


class VideoGame(models.Model):
    class VideoGameGenreChoices(models.TextChoices):
        ACTION_ADVENTURE = 'Action-Adventure', 'Action-Adventure'
        RPG = 'RPG', 'Role-Playing Game'
        FPS = 'FPS', 'First Person Shooter'
        MMO = 'MMO', 'MMO'
        STRATEGY = 'Strategy', 'Strategy'
        SPORTS = 'Sports', 'Sports'
        HORROR = 'Horror', 'Horror'
        FIGHTING = 'Fighting', 'Fighting'
        RACING = 'Racing', 'Racing'
        PLATFORMER = 'Platformer', 'Platformer'
        SURVIVAL = 'Survival', 'Survival'

    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )

    description = models.TextField(
        verbose_name='Description'
    )

    release_date = models.DateField(
        verbose_name='Release Date'
    )

    genre = models.CharField(
        max_length=100,
        choices=VideoGameGenreChoices.choices,
        verbose_name='Genre'
    )

    developer = models.ForeignKey(
        to=Developer,
        null=True,
        on_delete=models.SET_NULL,
        related_name='games',
        verbose_name='Developer'
    )

    poster = models.ImageField(
        upload_to='posters/',
        null=True,
        blank=True,
    )

    def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 1) if avg_rating is not None else None

    def __str__(self):
        return self.title


class MovieReview(Review):
        class Meta:
            constraints = [
                models.UniqueConstraint(fields=['user', 'movie'], name='unique_movie_review'),
            ]

        movie = models.ForeignKey(
            to=Movie,
            on_delete=models.CASCADE,
            related_name='reviews',
            verbose_name='Movie',
        )

        def __str__(self):
            return f'{self.user.username} gave {self.movie.title} a {self.rating}'


class VideoGameReview(Review):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'video_game'], name='unique_videogame_review'),
        ]

    video_game = models.ForeignKey(
        to=VideoGame,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Video Game'
    )

    def __str__(self):
        return f'{self.user.username} gave {self.video_game.title} a {self.rating}'