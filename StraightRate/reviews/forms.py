from django import forms

from StraightRate.reviews.models import VideoGameReview, MovieReview


class BaseMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['rating', 'comment']


class AddMovieReviewForm(BaseMovieReviewForm):
    def __init__(self, *args, **kwargs):
        super(AddMovieReviewForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs['placeholder'] = 'Write a movie review'


class BaseVideoGameReviewForm(forms.ModelForm):
    class Meta:
        model = VideoGameReview
        fields = ['rating', 'comment']


class AddVideoGameReviewForm(BaseVideoGameReviewForm):
    class Meta(BaseVideoGameReviewForm.Meta):
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write a comment'}),
        }


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=True,
    )