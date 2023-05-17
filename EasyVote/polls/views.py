from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Poll
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


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
def delete_poll(request, poll_id):
    if request.method == 'POST':
        poll = Poll.objects.get(id=poll_id)
        poll.delete()
    return redirect('manage_polls')
def submit_vote(request):
    if request.method == 'POST':
        choice_message = request.POST.get('choice_message')
        if choice_message == 'YES':
            choice = Choice.objects.get(choice_text='YES')
        else:
            choice = Choice.objects.get(choice_text='NO')
        choice.votes += 1
        choice.save()
        return JsonResponse({'result': 'success'})
    return JsonResponse({'result': 'error'})
def poll_results_data(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    yes_votes = poll.votes.filter(vote=True).count()
    no_votes = poll.votes.filter(vote=False).count()
    total_votes = poll.votes.count()

    if total_votes > 0:
        yes_votes_percent = (yes_votes / total_votes) * 100
        no_votes_percent = (no_votes / total_votes) * 100
    else:
        yes_votes_percent = no_votes_percent = 0

    response_data = {
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'yes_votes_percent': "{0:.1f}".format(yes_votes_percent),
        'no_votes_percent': "{0:.1f}".format(no_votes_percent),
        'total_votes': total_votes
    }

    return JsonResponse(response_data)
    
def view_results(request, poll_id):
    if not request.user.is_authenticated:
        return redirect('login')
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'polls/view_results.html', {'poll': poll})
