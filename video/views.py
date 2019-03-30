from django.shortcuts import render

# Create your views here.
def video(request):
	"""The video page"""
	return render(request, 'video.html')
