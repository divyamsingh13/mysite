from django.shortcuts import *
from blog.models import BlogPost,BlogPostForm
from datetime import datetime
from django.template import loader

# Create your views here.
from django.http import *
def index(request):
	#post=BlogPost(title="mocktitle" ,body="mockbody",timestamp=datetime.now())
	#return render_to_response("index.html",{'posts':[post]})
	#return HttpResponse("<h1> hbfh xfhdfhsfdbdf </h1>")
	posts=BlogPost.objects.all()
	
	context={'posts':posts,'form':BlogPostForm()}
	return render(request,"blog/index.html",context)
	#return render_to_response('index.html',{'posts':posts,'form':BlogPostForm()},RequestContext(request))





def create_blogpost(request):
	if request.method=='POST':
		form=BlogPostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.timestamp=datetime.now()
			post.save()
	return HttpResponseRedirect('/blog')		