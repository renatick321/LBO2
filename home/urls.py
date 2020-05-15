from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name='home'),
	path("popular/", views.popular, name="popular"),
	path("book_create/", views.book_create, name="book_create"),
	path("tag/<str:slug>/", views.get_tag, name="get_tag"),
	path("tags/", views.tag_list, name="tag_list"),
	path("genre/<str:slug>/", views.get_genre, name="get_genre"),
	path("genre/", views.genre_list, name="genre_list"),
	path("book/<int:book_id>/", views.book, name="book"),
	path("book/<int:book_id>/<int:number>/", views.chapter, name="chapter"),
]