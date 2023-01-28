import datetime
from django.db import models
from django.utils import timezone
from RestAp import settings


class Dish(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    img_of_dish = models.ImageField(upload_to='media/')

    TYPE_OF_DISH = [
        ('BRK', 'Breakfast'),
        ('LUN', 'Lunch'),
        ('DIN', 'Dinner'),
    ]

    type_of_dish = models.CharField(max_length=3, choices=TYPE_OF_DISH, default='LUN')

    def __str__(self):
        return self.title


class Review(models.Model):
    quote = models.TextField(max_length=500)
    customer_name = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='media/')

    RATING = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    rating = models.IntegerField(choices=RATING)

    def __str__(self):
        return self.customer_name


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    website = models.URLField()
    bio = models.TextField(max_length=200)
    avatar = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField(max_length=2048)
    article_img = models.ImageField(upload_to='media/')
    article_author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    CATEGORY = [
        ('RESTFOOD', 'Resaurant food'),
        ('TRAVNEWS', 'Travel news'),
        ('MDRNTECH', 'Modern technology'),
        ('PRODUCTS', 'Product'),
        ('INSPIRAT', 'Inspiration'),
        ('HLTHCARE', 'Health Care')
    ]

    category = models.CharField(max_length=8, choices=CATEGORY)

    def __str__(self):
        return self.article_title

    def was_published_recently():
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    comment_text = models.TextField(max_length=200)
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment_text
