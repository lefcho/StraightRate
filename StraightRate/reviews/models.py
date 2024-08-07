from django.db import models
from django.conf import settings


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

    def __str__(self):
        return f"{self.user.username} - {self.rating}"


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
    class GenreChoices(models.TextChoices):
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
        choices=GenreChoices.choices,
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

    def __str__(self):
        return self.title


class VideoGame(models.Model):
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

    def __str__(self):
        return self.title


class MovieReview(Review):
    movie = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Movie'
    )


class VideoGameReview(Review):
    video_game = models.ForeignKey(
        to=VideoGame,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Video Game'
    )