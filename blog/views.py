from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	context = {
		'posts' : posts,
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})

posts = [
	{
		'author':'TimothyYJH',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted' : 'November 21st of 2021',
	},
	{
		'author':'HazelYZ',
		'title':'Blog Post 2',
		'content':'Second post content',
		'date_posted' : 'November 31st of 2021',
	},

]