from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from . models import Users, Task
from django.contrib.auth.models import User
from django.urls import reverse




def home(request):
    return render(request, 'tasks/home.html')




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user_profile, created = Users.objects.get_or_create(user=user)
                return redirect('tasks:dashboard', user_id=user_profile.id)
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})




def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user_profile = Users.objects.create(user=user, date_joined=datetime.now())
            return redirect('tasks:dashboard', user_id=user_profile.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('tasks:home'))



@login_required
def create_task(request):   
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user.users
            task.save()
            if task.user:
                return redirect(reverse('tasks:dashboard', args=[task.user.id]))
    return render(request, 'tasks/create_task.html', {'form': form})





@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = request.POST.get('completed') == 'true'
        if request.FILES.get('image'):
            task.image = request.FILES['image']
        task.save()
        return redirect(reverse('tasks:dashboard', args=[task.user.id]))
    elif request.method == 'DELETE':
        task.delete()
        return redirect(reverse('tasks:dashboard', args=[task.user.id]))
    else:
        context = {'task': task}
        return render(request, 'tasks/update_task.html', context)


@login_required
def dashboard(request, user_id):
    user_profile = Users.objects.get(id=user_id)
    tasks = Task.objects.filter(user=user_profile).order_by('created_at')
    return render(request, 'tasks/dashboard.html', {'user_profile': user_profile, 'tasks': tasks})











@login_required
def delete_task(request, task_id):
    # your delete_task view code here
    pass



