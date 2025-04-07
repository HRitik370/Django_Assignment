from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer
from .forms import UserRegisterForm, QuestionForm, AnswerForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'qa_app/register.html', {'form': form})

def home(request):
    questions = Question.objects.all()
    return render(request, 'qa_app/home.html', {'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, 'Your question has been posted!')
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'qa_app/ask_question.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'You need to log in to post an answer.')
            return redirect('login')
            
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.user = request.user
            new_answer.question = question
            new_answer.save()
            messages.success(request, 'Your answer has been posted!')
            return redirect('question_detail', pk=question.pk)
    else:
        answer_form = AnswerForm()
        
    context = {
        'question': question,
        'answers': answers,
        'answer_form': answer_form
    }
    return render(request, 'qa_app/question_detail.html', context)

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
        
    return HttpResponseRedirect(reverse('question_detail', args=[answer.question.pk]))

@login_required
def profile(request):
    user_questions = Question.objects.filter(user=request.user)
    user_answers = Answer.objects.filter(user=request.user)
    liked_answers = Answer.objects.filter(likes=request.user)
    
    context = {
        'user_questions': user_questions,
        'user_answers': user_answers,
        'liked_answers': liked_answers
    }
    
    return render(request, 'qa_app/profile.html', context)