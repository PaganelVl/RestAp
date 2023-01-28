from django.contrib import admin
from .models import Dish, Review, Article, Comment


admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(Article)
admin.site.register(Comment)
