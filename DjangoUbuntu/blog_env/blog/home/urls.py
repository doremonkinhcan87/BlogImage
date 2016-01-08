from django.conf.urls import patterns, url
from django.conf import settings
from home import views as home_views

urlpatterns = [
	url(
		r'^$',
		home_views.index,
		name='index'),
	url(
		r'^auth$',
		home_views.auth,
		name='auth'),
	url(
		r'^media/(?P<path>.*)$', 
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
	] 