from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import User

# Create your views here.

def hello(request):
    return render(request, "home.html")

def users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', {'users': all_users})

def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        user = User.objects.create(name=name, email=email, role=role)
        return redirect('users')
        # return JsonResponse({'message': 'User created successfully!'})
    return render(request, 'new_users.html')

def user_details(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_details.html', {'user': user})
