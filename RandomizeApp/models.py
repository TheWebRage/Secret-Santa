from django.db import models


class User(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)

    # Address
    city = models.CharField(null=True, max_length=100)
    street = models.CharField(null=True, max_length=100)
    state = models.CharField(null=True, max_length=100)
    zip = models.CharField(null=True, max_length=100)

    # Questionnaire
    hobbies = models.CharField(verbose_name="Hobbies", null=True, max_length=300)
    i_have_plenty_of = models.CharField(null=True, max_length=300, verbose_name='I have plenty of')
    i_would_like_more_of = models.CharField(null=True, max_length=300, verbose_name='I would like more of')
    favorite_treat = models.CharField(null=True, max_length=300, verbose_name='Favorite Treat')
    colors_in_home_or_room = models.CharField(null=True, max_length=300, verbose_name='Colors in home/room')
    something_i_am_hoping_for_christmas_but_have_not_told_anyone = models.CharField(null=True, max_length=300, verbose_name='Something I am hoping for christmas but have not told anyone')
    someone_who_knows_what_gifts_i_like = models.CharField(null=True, max_length=300, verbose_name='Someone who knows what gifts I like')
    shirt_size = models.CharField(null=True, max_length=300, verbose_name='Shirt size')
    pants_size = models.CharField(null=True, max_length=300, verbose_name='Pants size')
    shoe_size = models.CharField(null=True, max_length=300, verbose_name='Shoe size')
    favorite_gift_i_have_gotten = models.CharField(null=True, max_length=300, verbose_name='Favorite gift I have gotten')
    amazon_wishlist_link = models.CharField(null=True, max_length=300, verbose_name='Amazon wishlist link')

    assigned_to = models.ManyToManyField('self', null=True, related_name='assigned', symmetrical=False)