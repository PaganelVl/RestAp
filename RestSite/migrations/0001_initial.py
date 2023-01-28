# Generated by Django 4.1.5 on 2023-01-11 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField(max_length=2048)),
                ('article_img', models.ImageField(upload_to='media/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('RESTFOOD', 'Resaurant food'), ('TRAVNEWS', 'Travel news'), ('MDRNTECH', 'Modern technology'), ('PRODUCTS', 'Product'), ('INSPIRAT', 'Inspiration'), ('HLTHCARE', 'Health Care')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField()),
                ('img_of_dish', models.ImageField(upload_to='media/')),
                ('type_of_dish', models.CharField(choices=[('BRK', 'Breakfast'), ('LUN', 'Lunch'), ('DIN', 'Dinner')], default='LUN', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=500)),
                ('customer_name', models.CharField(max_length=60)),
                ('avatar', models.ImageField(upload_to='media/')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('bio', models.TextField(max_length=200)),
                ('avatar', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestSite.article')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestSite.user')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestSite.user'),
        ),
    ]
