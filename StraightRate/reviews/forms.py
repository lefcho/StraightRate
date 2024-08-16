from django import forms

from StraightRate.reviews.models import VideoGameReview, MovieReview


class BaseMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'comment']

    widgets = {
        'comment': forms.TextInput(attrs={'placeholder': 'Write a comment'}),
    }


class AddMovieReviewForm(BaseMovieReviewForm):
    pass


class BaseVideoGameReviewForm(forms.ModelForm):
    class Meta:
        model = VideoGameReview
        fields = ['rating', 'comment']

    widgets = {
        'comment': forms.TextInput(attrs={'placeholder': 'Write a comment'}),
    }


class AddVideoGameReviewForm(BaseVideoGameReviewForm):
    pass