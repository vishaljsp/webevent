from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('corporate-events',views.corporate.as_view(),name="corporate"),
    path('contact-us',views.contact.as_view(),name="contact"),
    path('about-us',views.about.as_view(),name="about"),
    path('gallery',views.gallery.as_view(),name="gallery"),
    path('wedding-events',views.wedding.as_view(),name="wedding"),
    path('party-oragnizer',views.party.as_view(),name="party"),
    path('artist-management',views.artist.as_view(),name="artist"),
    path('propety-expo',views.propety.as_view(),name="propety"),
    path('catering-ervices',views.cateringervices.as_view(),name="cateringervices"),
    path('fest',views.fest.as_view(),name="fest"),

]
