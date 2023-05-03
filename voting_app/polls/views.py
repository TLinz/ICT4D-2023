from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Poll



def index(request):
    if request.user.is_authenticated:
        return redirect('manage_polls')
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('manage_polls')
        else:
            return render(request, 'polls/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'polls/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def manage_polls(request):
    if not request.user.is_authenticated:
        return redirect('login')
    polls = Poll.objects.filter(user=request.user)
    return render(request, 'polls/manage_polls.html', {'polls': polls})

def create_poll(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        poll = Poll(
            user=request.user,
            question=request.POST['question'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            phone_number=request.POST['phone_number']
        )
        poll.save()
        return redirect('manage_polls')
    else:
        return render(request, 'polls/create_poll.html')

def view_results(request, poll_id):
    if not request.user.is_authenticated:
        return redirect('login')
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'polls/view_results.html', {'poll': poll})
