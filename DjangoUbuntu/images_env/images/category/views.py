from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from category.models import Category
from category.models import CategoryForm

# Create your views here.
# def index(request):
   # return render(
       # request,
       # 'category/index.html'
   # )

#Form nhap lieu
def index(request):
   data = {}
   if request.method == 'POST':
       form = CategoryForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/category/success')
   else:
       form = CategoryForm()
   list_item = Category.objects.all()
   data['id'] = None
   data['list_item'] = list_item
   data['form'] = form
   return render(
       request,
       'category/index.html',
       data
   )
   
def update_item(request, id):
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
           return HttpResponseRedirect('/category/success')
   list_item = Category.objects.all()
   data['id'] = id
   data['list_item'] = list_item
   data['form'] = form
   return render(
       request,
       'category/index.html',
       data
   )

def remove_item(request, id):
   data = {}
   try:
       selected_item = Category.objects.get(pk=id)
       selected_item.delete()
       form = CategoryForm()
   except Category.DoesNotExist:
       raise Http404("This item not exist.")
   list_item = Category.objects.all()
   data['id'] = None
   data['list_item'] = list_item
   data['form'] = form
   return HttpResponseRedirect('/category', data)

def success(request):
   return render(
       request,
       'category/success.html'
   )