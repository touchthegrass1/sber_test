from django.urls import path

from . import views

app_name = 'visited_websites'

urlpatterns = [
    path('visited_links', views.save_visited_links, name='save_visited_links'),
    path('visited_domains', views.get_visited_domains, name='get_visited_domains'),
]
