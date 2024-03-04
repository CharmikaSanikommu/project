from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.database,name="database"),
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('imagesPage',views.imagesPage,name="imagesPage"),
    path('animals',views.animals,name="animals"),
    path('basic',views.basic,name="basic"),
    path('medium',views.medium,name="medium"),
    path('advanced',views.advanced,name="advanced"),
    path('alphabets',views.alphabets,name="alphabets"),
    path('alphabets_small',views.alphabets_small,name="alphabets_small"),
    path('alphabets_capital',views.alphabets_capital,name="alphabets_capital"),
    path('numbers',views.numbers,name="numbers"),
    path('numbers_zero_nine',views.numbers_zero_nine,name="numbers_zero_nine"),
    path('numbers_words',views.numbers_words,name="numbers_words"),
    path('shapes',views.shapes,name="shapes"),
    path('shapes_and_names',views.shapes_and_names,name="shapes_and_names"),
    path('colors',views.colors,name="colors.html"),
    path('states',views.states,name="states.html"),
    path('indian_states',views.indian_states,name="indian_states.html"),
    path('indian_capitals',views.indian_capitals,name="indian_capitals.html"),
]
