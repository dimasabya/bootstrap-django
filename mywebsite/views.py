from django.shortcuts import render

def index(request):
    context = {
        'title': 'Django Bootstrap',
        'heading': 'Selamat Datang',
        'subheading': 'di Django Bootstrap',
    }
    return render(request,'index.html',context)