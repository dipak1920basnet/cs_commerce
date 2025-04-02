from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

#Models for Category

class Category(models.Model):
    category_field = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_field}"
    
# Models for acution_listings
class Auction_listing(models.Model):
    
    # a title for the listing,
    title = models.CharField(max_length=30)
    #  a text-based description, 
    description = models.CharField(max_length=300) 
    # what the starting bid should be.
    starting_bid = models.IntegerField(blank=False)
    # Users should also optionally be able to provide a URL for an image
    image_url = models.URLField(null=True, blank=True)

    # and/or a category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    is_active = models.BooleanField(default=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comments")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name='onwatchlist')

    def __str__(self):
        return f"{self.title} {self.description}"
    
