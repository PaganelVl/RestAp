from django.shortcuts import render
from RestSite.models import Dish, Review
from .forms import BookATable


def index(request):
    menu_brk = Dish.objects.filter(type_of_dish__exact='BRK').order_by('?')[:6]
    menu_lun = Dish.objects.filter(type_of_dish__exact='LUN').order_by('?')[:6]
    menu_din = Dish.objects.filter(type_of_dish__exact='DIN').order_by('?')[:6]

    testimonials = Review.objects.filter(rating__exact='5').order_by('?')[:6]

    context = {
        'menu_brk': menu_brk,
        'menu_lun': menu_lun,
        'menu_din': menu_din,
        'testimonials': testimonials,
        'form': BookATable()
    }

    return render(
        request,
        'index.html',
        context=context    
    )


def menu(request):
    menu_brk = Dish.objects.filter(type_of_dish__exact='BRK')
    menu_lun = Dish.objects.filter(type_of_dish__exact='LUN')
    menu_din = Dish.objects.filter(type_of_dish__exact='DIN')

    testimonials = Review.objects.filter(rating__exact='5').order_by('?')[:6]

    context = {
        'menu_brk': menu_brk,
        'menu_lun': menu_lun,
        'menu_din': menu_din,
        'testimonials': testimonials,
        'form': BookATable()
    }

    return render(
        request,
        'menu.html',
        context=context    
    )


def about(request):
    testimonials = Review.objects.filter(rating__exact='5').order_by('?')[:6]

    context = {
        'testimonials': testimonials,
        'form': BookATable()
    }

    return render(
        request,
        'about.html',
        context=context    
    )


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
