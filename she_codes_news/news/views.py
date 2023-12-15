# from django.forms.models import BaseModelForm
# from django.http import HttpResponse
from typing import Any
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:6]
        return context
    
class StoryView(generic.DetailView):
  model = NewsStory
  template_name = 'news/story.html'
  context_object_name = 'story'

class AddStoryView(generic.CreateView):
    model = NewsStory
    form_class = StoryForm 
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# class DeleteStoryView(UserPassesTestMixin, generic.DeleteView):
#     model = NewsStory
#     form_class = StoryForm
#     template_name = 'news/deletestory.html'
#     success_url = reverse_lazy('news:index')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
#     def test_func(self):
#         return self.request.user == self.get_object().author 
    
#     def deletestory(request, pk):
#         NewsStory = get_object_or_404(NewsStory, pk=pk, author=request.User)
#         if request.method == 'POST':
#             NewsStory.delete()
#             return redirect('news:index') 
#         return render(request, 'news/deletestory.html',{'story':NewsStory})

        

# class EditStoryView(UserPassesTestMixin, generic.UpdateView):
#     model = NewsStory
#     form_class = StoryForm 
#     template_name = 'news/editStory.html'
#     success_url = reverse_lazy('news:index')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
#     def test_func(self):
#         return self.request.user == self.get_object().author
      
class AuthorStoryView(generic.ListView):
  model = NewsStory
  template_name = 'news/authorstoryview.html'
  context_object_name = 'author_stories'
  
  def get_queryset(self):
     return NewsStory.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
                                          # self.kwargs['pk'])
#   def AuthorStoryView(request, author_id):
#       Author = Author.objects.get(pk=author_id)
  

# NewsStorystories = NewsStory.objects.filter(author=Author)

# Context = {
#         'Author':Author,
#         'stories': NewsStory,
#     }
# return render(request, 'authorstoryview.html', context)
class deleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

class updateStoryView(generic.UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'image', 'content']
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')