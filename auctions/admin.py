from django.contrib import admin

from .models import Category, User, Auction_listing 

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Auction_listing)