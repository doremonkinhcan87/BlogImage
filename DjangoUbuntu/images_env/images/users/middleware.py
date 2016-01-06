from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from users.models import Users
from django.conf import settings
from django.shortcuts import render

class ImageMiddleware(object):
	def process_request(self, request):	
		# allowed_ips = ['192.168.1.1', '192.168.163.1'] 
		# ip = request.META.get('REMOTE_ADDR') 
		# if ip not in allowed_ips:
			# raise Http404("This is ip don't allow %s " %ip) 
		# return None
		# a = request.COOKIES['sessionid']
		# print (a)
		s = request.session.get('users_id', None)
		s1 = request.session.get('users_role', None)
		if request.method == 'POST':
			email = request.POST.get('email', None)
			password = request.POST.get('password', None)
			try:
				users = Users.objects.get(email=email)
				if users.email == email and users.password == password :	
					request.session['users_id'] = users.id
					request.session['users_role'] = users.role
			except Users.DoesNotExist:
				pass
		if s:
			if s1 == "admin":
				return None
				del request.session['users_role']
			del request.session['users_id']
		return None