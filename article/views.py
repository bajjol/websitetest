from django.shortcuts import render

# Create your views here.
def article(request):
	"""The article page"""
	return render(request, 'article.html')
