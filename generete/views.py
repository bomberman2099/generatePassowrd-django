from django.shortcuts import render

def TestView(request):
    return render(request, 'index.html')