from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.

def blog_home(request):
    blogs = models.blog.objects.all()
    return render(request, 'blog/blog_home.html', {'blogs':blogs})

def blog_dtl(request, pk):
    blog = get_object_or_404(models.blog, pk=pk)
    return render(request, 'blog/blog_dtl.html', {'blog':blog})
