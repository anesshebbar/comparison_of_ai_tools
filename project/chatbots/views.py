from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Chatbot, Review
from .forms import ReviewForm, UserRegistrationForm
from django.contrib.auth import login, logout
from django.db.models import Q

def home(request):
    return render(request, 'novels/home.html')

def chatbot_list(request):
    query = request.GET.get('q', '')
    novels = Novel.objects.all()
    
    if query:
        chatbot = chatbot.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query)
        )
    
    return render(request, 'chatbots/chatbot_list.html', {'chatbots': chatbots, 'query': query})


def chatbot_detail(request, novel_id):
    print(f"Viewing details for novel ID: {novel_id}")
    novel = get_object_or_404(Novel, id=novel_id)  # <--- ici
    reviews = novel.reviews.all().order_by('-created_at')
    
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    else:
        user_review = None
    
    return render(request, 'novels/novel_detail.html', {
        'novel': novel,
        'reviews': reviews,
        'user_review': user_review
    })

@login_required
def add_review(request, novel_id):
    chatbot = get_object_or_404(Chatbot, id=chatbot_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.chatbot = chatbot
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('chatbot_detail', chatbot_id=chatbot_id)
    else:
        form = ReviewForm()
    
    return render(request, 'novels/add_review.html', {'form': form, 'chatbot': chatbot})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('chatbot_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
def logout_request(request):
    logout(request)
    return redirect('login')