from django import forms
from .models import User


class UserForm(forms.ModelForm):
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)
    state = forms.CharField(required=False)
    zip = forms.CharField(required=False)
    hobbies = forms.CharField(required=False)
    i_have_plenty_of = forms.CharField(required=False)
    i_would_like_more_of = forms.CharField(required=False)
    favorite_treat = forms.CharField(required=False)
    colors_in_home_or_room = forms.CharField(required=False)
    something_i_am_hoping_for_christmas_but_have_not_told_anyone = forms.CharField(required=False)
    someone_who_knows_what_gifts_i_like = forms.CharField(required=False)
    shirt_size = forms.CharField(required=False)
    pants_size = forms.CharField(required=False)
    shoe_size = forms.CharField(required=False)
    favorite_gift_i_have_gotten = forms.CharField(required=False)
    amazon_wishlist_link = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'city', 'street', 'state', 'zip', 'hobbies', 'i_have_plenty_of', 'i_would_like_more_of', 'favorite_treat', 'colors_in_home_or_room', 'something_i_am_hoping_for_christmas_but_have_not_told_anyone',
                  'someone_who_knows_what_gifts_i_like', 'shirt_size', 'pants_size', 'shoe_size', 'favorite_gift_i_have_gotten', 'amazon_wishlist_link']