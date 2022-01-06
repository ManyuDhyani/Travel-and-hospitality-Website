from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(30)(home), name='home'),
    path('articles', articles, name='articles'),
    path('articles/<slug:slug_text>', article),
    path('article-form', article_form, name='articleform'),
    path('terms-and-conditions', terms, name='terms'),
    path('cancellation-policy', Cancellation, name='cancellation'),
    path('privacy-policy', privacy, name='privacy'),
    path('disclaimer', disclaimer, name='disclaimer'),
    path('about-us', aboutus, name='aboutUs'),
    path('contacts-us', contacts, name='contacts'),
    path('career', jobs, name='career'),
    path('activities', activities, name='activities'),
    path('treks/<slug:slug_text>', trek),
    path('treks', trek_main, name='treks'),
    path('village-tours/<slug:slug_text>', VillageTour),
    path('village-tours', VillageTour_main, name='VillageTours'),
    path('inquiry', inquiry, name='inquiry'),
    path('gallery', gallery, name='gallery'),
    path('create-package-form', create_package, name='create_package'),
    path('upcoming-events', upcoming_event, name='events'),
    path('book-a-spot', upcoming_event_form, name='eventForm'),
    path('adventure-sports', adventure_sports_manyu, name='adventure_manyu'),
    path('community-work', community_work, name='community'),
    path('about-trekking', about_Trek, name='abouttrek'),
    path('about-village-tours', about_Village, name='aboutvillgae'),
    path('search', search, name='search'),
    path('testimonials', testimonials, name='testimonials'),
    #path('feedback', feedback, name='feedback'),
]
