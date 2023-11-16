from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup_profile(request):
    return render(request, 'BookFair/signup_profile.html')
