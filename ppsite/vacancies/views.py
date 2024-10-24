from django.shortcuts import render, get_object_or_404
from .models import Vacancies
from django.http import Http404
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm, VacancyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
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
    
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Vacancies.published.annotate(
                search=SearchVector('name', 'body'),
            ).filter(search=query)
    return render(request,
            'vacancies/post/search.html',
            {'form': form,
            'query': query,
            'results': results})

class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancies
    form_class = VacancyForm
    template_name = 'vacancies/post/vacancy_form.html'
    success_url = reverse_lazy('vacancies/post/list.html')  # Укажите URL для перенаправления после успешного создания вакансии

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем текущего пользователя как автора вакансии
        return super().form_valid(form)

class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancies
    form_class = VacancyForm
    template_name = 'vacancies/post/vacancy_form.html'
    success_url = reverse_lazy('vacancies/post/list.html')  # Укажите URL для перенаправления после успешного создания вакансии

    def form_valid(self, form):
        form.instance.author = self.request.user  # Устанавливаем текущего пользователя как автора вакансии
        return super().form_valid(form)