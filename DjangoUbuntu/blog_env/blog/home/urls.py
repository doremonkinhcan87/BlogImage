from django.conf.urls import patterns, url
from django.conf import settings
from home import views as home_views

urlpatterns = [
	url(
		r'^$',
		home_views.index,
		name='index'),
	url(
		r'^admin$',
		home_views.admin,
		name='admin'),
	url(
		r'^update/(?P<id>[\d]+)$',
		home_views.update_admin,
		name='update'),
	url(
		r'^remove/(?P<id>[\d]+)$',
		home_views.remove_admin,
		name='remove'),
	url(
		r'^auth$',
		home_views.auth,
		name='auth'),
	
	url(
		r'^media/(?P<path>.*)$', 
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
		
	url(
		r'^login$',
		home_views.login,
		name='login'),
	url(
		r'^update_item/(?P<id>[\d]+)$',
		home_views.update_item,
		name='update_item'),
	url(
		r'^remove_item/(?P<id>[\d]+)$',
		home_views.remove_item,
		name='remove_item'),
	url(
		r'^logout$',
		home_views.logout,
		name='logout'),

	] 