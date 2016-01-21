from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home.models import Document
from home.models import DocumentForm
from home.models import Users
from home.models import UsersForm
from home.models import Group
from home.models import GroupForm
from home.models import Tags
from home.models import TagsForm
from home.models import Category
from home.models import CategoryForm
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator

def blog(request):
	# Handle file upload
	#tags = Tags.objects.all()
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document()
			newdoc.docfile = request.FILES['docfile']
			newdoc.title = request.POST['title']
			newdoc.users_id = request.POST['users']
			newdoc.summary = request.POST['summary']
			newdoc.content = request.POST['content']
			newdoc.publish = request.POST['publish']
			newdoc.category_id = request.POST['category']		
			request.session['users_id'] = newdoc.users_id
			newdoc = form.save(commit=False)
			newdoc.save()
			form.save_m2m()
			return HttpResponseRedirect('/blog')
	else:
		form = DocumentForm()  # A empty, unbound form
	# Load documents for the index page
	documents = Document.objects.all()
	paginator = Paginator(documents, 4)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		documents = paginator.page(page)
	except(EmptyPage, InvalidPage):
		documents = paginator.page(paginator.num_pages)
		
	# Render index page with the documents and the form
	return render_to_response(
		'home/blog.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)
	
# def update_blog(request, id):
	# try:
		# selected_item = Document.objects.get(pk=id)
		# form = DocumentForm(instance=selected_item)
	# except Document.DoesNotExist:
		# raise Http404("This item not exist.")
	# if request.method == 'POST':
		# form = DocumentForm(request.POST or None, request.FILES or None, instance=selected_item)
		# if form.is_valid():
			# form.save()
			# return HttpResponseRedirect('/blog')
	# documents = Document.objects.all()
	# return render_to_response(
		# 'home/blog.html',
		# {'documents': documents, 'form': form},
		# context_instance=RequestContext(request)
	# )

def update_blog(request, id):
	data = {}
	try:
		selected_item = Document.objects.get(pk=id)
		form = DocumentForm(instance=selected_item)
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = DocumentForm(request.POST or None, request.FILES or None,instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog')
	documents = Document.objects.all()
	data['id'] = id
	data['documents'] = documents
	data['form'] = form
	return render(
		request,
		'home/blog.html',
		data
	)
	
def remove_blog(request, id):
	try:
		selected_item = Document.objects.get(pk=id)
		selected_item.delete()
		form = DocumentForm()
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	documents = Document.objects.all()
	return HttpResponseRedirect('/blog')

def index(request):
	# Handle file upload
	# s = request.session.get('users_id', None)
	# if not s:
		# return render(
				# request,
				# 'home/index.html'
			# )
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document()
			newdoc.docfile = request.FILES['docfile']
			newdoc.title = request.POST['title']
			#request.session['users_id'] = newdoc.users_id
			newdoc.save()
			return HttpResponseRedirect('/')
	else:
		form = DocumentForm()
		
	documents = Document.objects.all()
	posts_list = Document.objects.all()

	paginator = Paginator(posts_list, 12)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	return render_to_response(
		'home/index.html',
		{'documents': documents, 'form': form,'posts': posts,},
		context_instance=RequestContext(request)
	)

#trang tao user
def users(request):
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
				return HttpResponseRedirect('/users')
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
		'home/users.html',
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
           return HttpResponseRedirect('/users')
   list_item = Users.objects.all()
   data['id'] = id
   data['list_item'] = list_item
   data['form'] = form
   return render(
       request,
       'home/users.html',
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
   return HttpResponseRedirect('/users', data)

def auth(request):
	s = request.session.get('users_id',None)
	if s:
		return HttpResponseRedirect('/users')
	if request.method == 'POST':
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and users.password == password:	
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/blog')
			else:
				return HttpResponseRedirect('/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/auth')
	return render(
		request,
		'home/auth.html'
	)
		
def tags(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = TagsForm(request.POST)
		if form.is_valid():
			newdoc = Tags()
			newdoc.users_id = request.POST['users']
			newdoc.name = request.POST['name']
			request.session['users_id'] = newdoc.users_id
			newdoc.save()
			return HttpResponseRedirect('/tags')
	else:
		form = TagsForm()
	tags = Tags.objects.all()
	return render_to_response(
		'home/tags.html',
		{'tags': tags, 'form': form},
		context_instance=RequestContext(request)
	)
	
def update_tags(request, id):
	data = {}
	try:
		selected_item = Tags.objects.get(pk=id)
		form = TagsForm(instance=selected_item)
	except Tags.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = TagsForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tags')
	tags = Tags.objects.all()
	data['id'] = id
	data['tags'] = tags
	data['form'] = form
	return render(
		request,
		'home/tags.html',
		data
	)

def remove_tags(request, id):
	try:
		selected_item = Tags.objects.get(pk=id)
		selected_item.delete()
		form = TagsForm()
	except Tags.DoesNotExist:
		raise Http404("This item not exist.")
	tags = Tags.objects.all()
	return HttpResponseRedirect('/tags')
	
def category(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			newdoc = Category()
			newdoc.users_id = request.POST['users']
			newdoc.name = request.POST['name']
			newdoc.description = request.POST['description']
			request.session['users_id'] = newdoc.users_id
			newdoc.save()
			return HttpResponseRedirect('/category')
	else:
		form = CategoryForm()
	categorys = Category.objects.all()
	return render_to_response(
		'home/category.html',
		{'categorys': categorys, 'form': form},
		context_instance=RequestContext(request)
	)
	
def update_category(request, id):
	data = {}
	try:
		selected_item = Category.objects.get(pk=id)
		form = CategoryForm(instance=selected_item)
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = CategoryForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category')
	categorys = Category.objects.all()
	data['id'] = id
	data['categorys'] = categorys
	data['form'] = form
	return render(
		request,
		'home/category.html',
		data
	)

def remove_category(request, id):
	try:
		selected_item = Category.objects.get(pk=id)
		selected_item.delete()
		form = CategoryForm()
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	categorys = Category.objects.all()
	return HttpResponseRedirect('/category')

def group(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			newdoc = Group()
			newdoc.users_id = request.POST['users']
			newdoc.name = request.POST['name']
			request.session['users_id'] = newdoc.users_id
			newdoc = form.save(commit=False)
			newdoc.save()
			form.save_m2m()
			return HttpResponseRedirect('/group')
	else:
		form = GroupForm()
	groups = Group.objects.all()
	return render_to_response(
		'home/group.html',
		{'groups': groups, 'form': form},
		context_instance=RequestContext(request)
	)
	
def update_group(request, id):
	data = {}
	try:
		selected_item = Group.objects.get(pk=id)
		form = GroupForm(instance=selected_item)
	except Group.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = GroupForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group')
	groups = Group.objects.all()
	data['id'] = id
	data['groups'] = groups
	data['form'] = form
	return render(
		request,
		'home/group.html',
		data
	)

def remove_group(request, id):
	try:
		selected_item = Group.objects.get(pk=id)
		selected_item.delete()
		form = GroupForm()
	except Group.DoesNotExist:
		raise Http404("This item not exist.")
	groups = Group.objects.all()
	return HttpResponseRedirect('/group')
	
def logout(request):
	try:
		del request.session['users_id']
	except KeyError:
		pass
	return render(
		request,
		'home/auth.html'
		)

def test(request):
	return render(
		request,
		'home/test.html'
		)

