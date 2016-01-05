from django.conf.urls import url
from django.contrib import admin
from home import views as home_views

urlpatterns = [
	url(
		r'^$',
		home_views.index,
		name='index'),
]