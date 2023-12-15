from django.urls import path
from .views import CreateAccountView, author_profile, articles_by_author

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('author/<int:id>/', author_profile, name='author_profile'),
    path('author/<int:id>/articles/', articles_by_author, name='articles_by_author')
    ]