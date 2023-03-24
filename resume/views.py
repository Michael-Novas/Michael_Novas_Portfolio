from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def about(request):
	f_name = "Michael"
	l_name = "Novas"
	return render(request, "about.html", {'first_name': f_name, 'last_name': l_name})

