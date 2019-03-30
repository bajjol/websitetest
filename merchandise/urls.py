from django.conf.urls import url
from . import views
urlpatterns = [
	# Home page
	url(r'^$', views.merchandise, name='merchandise'),
]
