from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import Users
from users.models import UsersForm
from django.contrib.auth.hashers import make_password, check_password

#Form nhap lieu
def login(request):
	form = UsersForm(request.POST)
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/login/auth')
	data = {}
	data['error_massage']=""
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		password_password =  make_password(password)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and check_password("password", password_password):	
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/login/')
			else:
				return HttpResponseRedirect('/login/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/login/auth')
	else :
		form = UsersForm()
	list_item = Users.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'users/login.html',
		data
	)
   
def update_item(request, id):
	data = {}
	try:
		selected_item = Users.objects.get(pk=id)
		form = UsersForm(instance=selected_item)
	except Users.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = UsersForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login/admin')
	list_item = Users.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'users/login.html',
		data
	)

def remove_item(request, id):
	data = {}
	try:
		selected_item = Users.objects.get(pk=id)
		selected_item.delete()
		form = UsersForm()
	except Users.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Users.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/login', data)

#Ham lay du lieu tu database
	
def admin(request):
	return render(
		request,
		'users/admin.html'
	)
	
def auth(request):
	s = request.session.get('users_id',None)
	if s:
		return HttpResponseRedirect('/login/')
	if request.method == 'POST':
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and users.password == password:	
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/login/')
			else:
				return HttpResponseRedirect('/login/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/login/auth')
	return render(
		request,
		'users/auth.html'
	)
	
def logout(request):
	try:
		del request.session['users_id']
	except KeyError:
		pass
	return render(
		request,
		'users/auth.html'
		)
