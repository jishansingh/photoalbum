from django import forms
from .models import todo_list
class todo_form(forms.Form):
	image=forms.FileField()
	name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={}))
	#widget={forms.TextInput(attr)}
