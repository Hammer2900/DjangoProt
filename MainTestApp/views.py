from django.shortcuts import render

# Create your views here.
def testo(request):
    return render(request, 'main.html')