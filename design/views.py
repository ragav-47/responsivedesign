from django.shortcuts import render

# Create your views here.

def responsivehome(request):
    context = {}
    return render(request, 'design/responsivehome.html', context)

def responsiveproduct(request):
    context = {}
    return render(request, 'design/responsiveproduct.html', context)

def responsivepeople(request):
    context = {}
    return render(request, 'design/responsivepeople.html', context)

def responsivecontactus(request):
    context = {}
    return render(request, 'design/responsivecontactus.html', context)

