from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.shortcuts import render

class ImageMiddleware(object):
	def process_request(self, request):	
		pass