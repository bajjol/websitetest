from django.conf.urls import url
from . import views
urlpatterns = [
	# Home page
	url(r'^$', views.video, name='video'),
]
