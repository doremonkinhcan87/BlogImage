from django.conf.urls import url
from django.contrib import admin
from users import views as users_views

urlpatterns = [
	url(
		r'^$',
		users_views.login,
		name='login'),
	url(
		r'^admin$',
		users_views.admin,
		name='admin'),
	url(
		r'^auth$',
		users_views.auth,
		name='auth'),
		
	url(
		r'^update/(?P<id>[\d]+)$',
		users_views.update_item,
		name='update'),
	url(
		r'^remove/(?P<id>[\d]+)$',
		users_views.remove_item,
		name='remove'),
	url(
		r'^logout$',
		users_views.logout,
		name='logout'),
]