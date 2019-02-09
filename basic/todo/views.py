from django.shortcuts import render,redirect
from .models import todo_list
from .forms import todo_form
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView
# Create your views here.
def index(request):
	tiktok=todo_list.objects.all()
	context={
		'todo':tiktok,'but':True
	}
	return render(request,'todo/index.html',context)
class add_photo(CreateView):
	model=todo_list
	fields=['name','image']

def delete_view(request):
	tiktok=todo_list.objects.all()
	context={
		'todo':tiktok,'but':False
	}
	return render(request,'todo/index.html',context)

class delete(DeleteView):
	model=todo_list
	success_url=reverse_lazy('todo:delete_view')