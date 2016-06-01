from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search_posts, name='search_posts'),
    url(r'^perform_search_posts_action/$', views.perform_search_posts_action, name='perform_search_posts_action'),
    url(r'^results/name=(?P<name>[a-zA-Z ]*)/state=(?P<state>[a-zA-Z ]*)/$', views.view_results, name='view_results'),
    url(r'^bad_search/reason=(?P<reason>[a-z]{5,6})', views.bad_search, name="bad_search"),
]