from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'KayakingZX/home.html')

def about(request):
    return render(request,'KayakingZX/about.html')

def timeline(request):
    return render(request,'KayakingZX/timeline.html')

def contact(request):
    return render(request,'KayakingZX/contact.html')

