from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
	'',
	url(
		r'^$',
		'home.views.index',
		name='index'),
	url(
		r'^media/(?P<path>.*)$', 
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
)
