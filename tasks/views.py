from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import login, authenticate


# Головна сторінка із списком завдань
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Створення нового завдання
@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

# Редагування завдання
@login_required
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

# Видалення завдання
@login_required
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Реєстрація
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправлення на головну сторінку
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# Логін
from django.contrib.auth import views as auth_views
login_view = auth_views.LoginView.as_view(template_name='tasks/login.html')

# Вихід
def logout_view(request):
    logout(request)
    return redirect('login')

# Головна сторінка
@login_required
def home(request):
    return render(request, 'tasks/home.html')

def custom_logout(request):
    logout(request)  # це завершує сесію користувача
    return redirect('/')  # редірект на головну сторінку
