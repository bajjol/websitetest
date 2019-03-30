from django.conf.urls import url
from dashboard import views
from . import views
urlpatterns = [
	# Home page
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^dashboard/edit/$', views.edit, name='edit'),
	url(r'^login/$', views.login, name='login'),
	url(r'^dashboard/pages/$', views.pages, name='pages'),
	url(r'^posts/$', views.posts, name='posts'),
	url(r'^users/$', views.users, name='users'),
]
