from django.shortcuts import render
from dashboard.models import PostForm

def dashboard(request):
	"""The home page"""
	return render(request, 'dashboard.html')
def edit(request):
	"""The home page"""
	return render(request, 'edit.html')
def login(request):
	"""The home page"""
	return render(request, 'login.html')
def pages(request):
	"""The home page"""
	return render(request, 'pages.html')
def posts(request):
	"""The home page"""
	return render(request, 'posts.html')
def users(request):
	"""The home page"""
	return render(request, 'users.html')

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('dashboard/')
	else:
		form = PostForm()
		return render(request, 'dashboard.html', {'form':form})
