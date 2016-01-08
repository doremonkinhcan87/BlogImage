from django.shortcuts import render

# def index(request):
	# return render(
		# request,
		# 'home/index.html'
	# )
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from home.models import Document
from home.models import DocumentForm


def index(request):
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
			return HttpResponseRedirect('/')
	else:
		form = DocumentForm()  # A empty, unbound form

	# Load documents for the index page
	documents = Document.objects.all()

	# Render index page with the documents and the form
	return render_to_response(
		'home/index.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def auth(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document()
			newdoc.docfile = request.FILES['docfile']
			newdoc.title = request.POST['title']
			newdoc.save()
			return HttpResponseRedirect('/auth')
	else:
		form = DocumentForm()
	documents = Document.objects.all()
	return render_to_response(
		'home/auth.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)