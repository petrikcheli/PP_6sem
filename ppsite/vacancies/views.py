from django.shortcuts import render, get_object_or_404
from .models import Vacancies
from django.http import Http404

# Create your views here.

def post_list(request):
    posts = Vacancies.published.all()

    return render(request, 'vacancies/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Vacancies,
                            id=id,
                            status=Vacancies.Status.PUBLISHED)
    
    return render(request,
                  'vacancies/post/detail.html',
                  {'post': post})
