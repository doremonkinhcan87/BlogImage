from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.shortcuts import render
from django.utils import translation
from django.utils.cache import patch_vary_headers

class ImageMiddleware(object):
	def process_request(self, request):	
		pass
class ProxyProcessing(object):

	def process_request(self, request):
		pass
		# language = request.META.get('HTTP_LANG', 'vi').lower()
		# translation.activate(language)
		# request.LANGUAGE_CODE = translation.get_language()
		# return None
		
class SessionBasedLocaleMiddleware(object):
	def process_request(self, request):
		if request.method == 'GET' and 'lang' in request.GET:
			language = request.GET['lang']
			request.session['language'] = language
		elif 'language' in request.session:
			language = request.session['language']
		else:
			language = translation.get_language_from_request(request)

		for lang in settings.LANGUAGES:
			if lang[0] == language:
				translation.activate(language)
				
		request.LANGUAGE_CODE = translation.get_language()
		
	def process_response(self, request, response):
		patch_vary_headers(response, ('Accept-Language',))
		if 'Content-Language' not in response:
			response['Content-Language'] = translation.get_language()
		translation.deactivate()
		return response
		