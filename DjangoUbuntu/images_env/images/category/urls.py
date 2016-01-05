from django.conf.urls import url
from category import views as category_views

urlpatterns = (
   url(
       r'^$',
       category_views.index,
       name='index'),
	url(
       r'^success$',
       category_views.success,
       name='success'),
	url(
	   r'^update/(?P<id>[\d]+)$',
	   category_views.update_item,
	   name='update'),
	url(
	   r'^remove/(?P<id>[\d]+)$',
	   category_views.remove_item,
	   name='remove'),

)