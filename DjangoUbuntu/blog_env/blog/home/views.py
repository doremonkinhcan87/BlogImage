from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home.models import Document
from home.models import DocumentForm
from home.models import Users
from home.models import UsersForm
from django.contrib.auth.hashers import make_password, check_password

def admin(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document()
			newdoc.docfile = request.FILES['docfile']
			newdoc.title = request.POST['title']
			newdoc.save()

			# Redirect to the document index after POST
			#return HttpResponseRedirect(reverse('views.index'))
			return HttpResponseRedirect('/admin')
	else:
		form = DocumentForm()  # A empty, unbound form

	# Load documents for the index page
	documents = Document.objects.all()

	# Render index page with the documents and the form
	return render_to_response(
		'home/admin.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)
	
def update_admin(request, id):
	try:
		selected_item = Document.objects.get(pk=id)
		form = DocumentForm(instance=selected_item)
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = DocumentForm(request.POST or None, request.FILES or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin')
	documents = Document.objects.all()
	return render_to_response(
		'home/admin.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def remove_admin(request, id):
	try:
		selected_item = Document.objects.get(pk=id)
		selected_item.delete()
		form = DocumentForm()
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	documents = Document.objects.all()
	return HttpResponseRedirect('/admin')

def index(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document()
			newdoc.docfile = request.FILES['docfile']
			newdoc.title = request.POST['title']
			newdoc.save()
			return HttpResponseRedirect('/')
	else:
		form = DocumentForm()
	documents = Document.objects.all()
	return render_to_response(
		'home/index.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

#trang tao user
def login(request):
	form = UsersForm(request.POST)
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
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
				return HttpResponseRedirect('/login')
			else:
				return HttpResponseRedirect('/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/auth')
	else :
		form = UsersForm()
	list_item = Users.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'home/login.html',
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
           return HttpResponseRedirect('/login')
   list_item = Users.objects.all()
   data['id'] = id
   data['list_item'] = list_item
   data['form'] = form
   return render(
       request,
       'home/login.html',
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

def auth(request):
	s = request.session.get('users_id',None)
	if s:
		return HttpResponseRedirect('/login')
	if request.method == 'POST':
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and users.password == password and users.role == 'admin':	
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/login')
			elif users.email == email and users.password == password and users.role == 'user':
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/admin')
			else:
				return HttpResponseRedirect('/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/auth')
	return render(
		request,
		'home/auth.html'
	)
	
def logout(request):
	try:
		del request.session['users_id']
	except KeyError:
		pass
	return render(
		request,
		'home/auth.html'
		)