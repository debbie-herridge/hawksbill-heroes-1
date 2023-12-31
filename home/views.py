from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))

def success_msg(request, args):
    amount = args
    return render(request, 'success', {'amount':amount})

def handler404(request, exception):
    """ 
    Error Handler 404 - Page Not Found
    """
    return render(request, "errors/404.html", status=404)
