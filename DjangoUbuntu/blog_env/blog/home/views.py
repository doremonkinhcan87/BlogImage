from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home.models import Document
from home.models import DocumentForm

def auth(request):
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
			return HttpResponseRedirect('/auth')
	else:
		form = DocumentForm()  # A empty, unbound form

	# Load documents for the index page
	documents = Document.objects.all()

	# Render index page with the documents and the form
	return render_to_response(
		'home/auth.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)
	
def update_auth(request, id):
	try:
		selected_item = Document.objects.get(pk=id)
		form = DocumentForm(instance=selected_item)
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = DocumentForm(request.POST or None, request.FILES or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/auth')
	documents = Document.objects.all()
	return render_to_response(
		'home/auth.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def remove_auth(request, id):
	try:
		selected_item = Document.objects.get(pk=id)
		selected_item.delete()
		form = DocumentForm()
	except Document.DoesNotExist:
		raise Http404("This item not exist.")
	documents = Document.objects.all()
	return HttpResponseRedirect('/auth')

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