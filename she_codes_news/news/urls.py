from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<int:pk>/', views.AuthorStoryView.as_view(), name='authorstories'),
    # path('delete/<int:pk>/', views.DeleteStoryView.as_view(), name='deletestory'), 
    # path('edit/<int:pk>/', views.EditStoryView.as_view(), name='editstory')
    path('<pk>/delete/', views.deleteStoryView.as_view(), name='deleteStory'),
    path('<pk>/update/', views.updateStoryView.as_view(), name='updateStory')]
# (r'^delete/(?P<pk>[0-9]+)/$', views.cat_delete, name='cat_delete')