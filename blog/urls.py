from django.conf.urls import *
from . import views
urlpatterns=[
url(r'^$',views.index,name='index')
,url(r'^create/',views.create_blogpost,name='create_blogpost'),]