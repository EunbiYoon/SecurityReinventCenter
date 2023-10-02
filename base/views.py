from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeView(request):
    return render(request, 'home.html')

def securityhomeView(request):
    return render(request, 'securityhome.html')

def reinventhomeView(request):
    return render(request, 'reinventhome.html')