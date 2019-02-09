from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

app_name='todo'
urlpatterns=[
	path('',views.index,name='index'),
	path('add/',views.add_photo.as_view(),name='add_photo'),
	path('del/',views.delete_view,name='delete_view'),
	path('del/<pk>/',views.delete.as_view(),name='delete'),
]

if settings.DEBUG==True:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
