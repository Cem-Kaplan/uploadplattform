from django.shortcuts import render

def show_home(request):
    return render(request, 'hauptseite/index.html')

def show_about(request):
    return render(request, 'hauptseite/about.html')
    
def show_upload(request):
    return render(request, 'hauptseite/upload.html')
    
def show_login(request):
    return render(request, 'hauptseite/login.html')