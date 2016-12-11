from django.conf.urls import url


from . import views

app_name = 'main'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^action/$', views.parse_request, name='parse_request'),
]
