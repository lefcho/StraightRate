from django import forms

from StraightRate.reviews.models import VideoGameReview, MovieReview


class BaseMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'comment']


class AddMovieReviewForm(BaseMovieReviewForm):
    widgets = {
        'comment': forms.TextInput(attrs={'placeholder': 'Write a comment'}),
    }


class BaseVideoGameReviewForm(forms.ModelForm):
    class Meta:
        model = VideoGameReview
        fields = ['rating', 'comment']


class AddVideoGameReviewForm(BaseVideoGameReviewForm):
    widgets = {
        'comment': forms.TextInput(attrs={'placeholder': 'Write a comment'}),
    }


class EditMovieReviewForm(BaseMovieReviewForm):
    pass


class EditVideoGameReviewForm(BaseMovieReviewForm):
    pass
