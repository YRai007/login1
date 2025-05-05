import os
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ContactForm, SubscriberForm, FavoriteGameForm
from .models import Contact, Subscriber, FavoriteGame

# --- Logging Decorator ---
def log_access(view_func):
    def wrapper(request, *args, **kwargs):
        print(f"[{datetime.datetime.now()}] View accessed: {view_func.__name__}")
        return view_func(request, *args, **kwargs)
    return wrapper

# --- Static Pages ---
@log_access
def home(request):
    return render(request, 'myapp/home.html', {'name': 'Yashvardhan Rai'})

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

# --- Contact Form ---
@log_access
def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thankyou')
    else:
        form = ContactForm()
    return render(request, 'myapp/contacts.html', {'form': form})

def contact_thankyou(request):
    return render(request, 'myapp/contact_thankyou.html')

# --- Static File Reader ---
def static_file(request):
    file_path = os.path.join(settings.BASE_DIR, 'myapp/static/info.txt')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("The file 'info.txt' was not found.", status=404)

# --- Newsletter ---
def newsletter_subscribe(request):
    success = False
    form = SubscriberForm()
    subscribers = None

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    elif request.method == 'GET' and request.GET.get('show') == 'subscribers':
        subscribers = Subscriber.objects.all()

    return render(request, 'myapp/newsletter.html', {
        'form': form,
        'success': success,
        'subscribers': subscribers
    })

# --- Favorite Game CRUD ---
def favorite_games_list(request):
    games = FavoriteGame.objects.all()
    return render(request, 'myapp/favorite_games_list.html', {'games': games})

def favorite_game_create(request):
    if request.method == 'POST':
        form = FavoriteGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('favorite_games_list')
        else:
            return render(request, 'myapp/favorite_game_form.html', {
                'form': form,
                'error': 'Form is invalid. Please correct the errors below.'
            })
    else:
        form = FavoriteGameForm()
    return render(request, 'myapp/favorite_game_form.html', {'form': form})

def favorite_game_update(request, pk):
    game = get_object_or_404(FavoriteGame, pk=pk)
    if request.method == 'POST':
        form = FavoriteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('favorite_games_list')
        else:
            return render(request, 'myapp/favorite_game_form.html', {
                'form': form,
                'error': 'Form is invalid. Please correct the errors below.'
            })
    else:
        form = FavoriteGameForm(instance=game)
    return render(request, 'myapp/favorite_game_form.html', {'form': form})

def favorite_game_delete(request, pk):
    game = get_object_or_404(FavoriteGame, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('favorite_games_list')
    return render(request, 'myapp/favorite_game_confirm_delete.html', {'game': game})

# --- Authentication Views ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid username or password'})
    return render(request, 'myapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
