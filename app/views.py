"""
Definition of views.
"""

from datetime import datetime
from .forms import FeedbackForm
from django.shortcuts import render
from django.http import HttpRequest
from .models import Blog
from .models import Blog, Comment
from .forms import CommentForm
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'app/index.html', {
        'title': 'Главная',
        'year': datetime.now().year,
    })

def about(request):
    return render(request, 'app/about.html', {
        'title': 'О поселке',
        'year': datetime.now().year,
    })

def contact(request):
    return render(request, 'app/contact.html', {
        'title': 'Контакты',
        'year': datetime.now().year,
    })
def links(request):
    return render(request, 'app/links.html', {
        'title': 'Полезные ресурсы',
        'year': datetime.now().year,
    })

def pool(request):
    data = None
    if request.method == 'POST': # Если пользователь нажал кнопку "Отправить"
        form = FeedbackForm(request.POST) # Берем данные из формы
        if form.is_valid(): # Если все заполнено правильно
            # Собираем данные в словарь, чтобы потом показать их пользователю
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['email'] = form.cleaned_data['email']
            data['age'] = form.cleaned_data['age']
            data['rating'] = form.cleaned_data['rating']
            
            liked = []
            if form.cleaned_data['liked_land']: liked.append('Участки')
            if form.cleaned_data['liked_nature']: liked.append('Природа')
            if form.cleaned_data['liked_infra']: liked.append('Инфраструктура')
            data['liked'] = ", ".join(liked) if liked else "Ничего не выбрано"
            
            data['interest'] = form.cleaned_data['interest']
            data['message'] = form.cleaned_data['message']
            
            form = None # Скрываем форму, чтобы показать благодарность
    else:
        form = FeedbackForm() # Если страница только открылась, показываем пустую форму

    return render(request, 'app/pool.html', {
        'title': 'Обратная связь',
        'form': form,
        'data': data,
        'year': datetime.now().year,
    })

def blog(request):
    posts = Blog.objects.all().order_by('-posted')
    return render(request, 'app/blog.html', {
        'title': 'Блог о поселке ВолгаПремиум',
        'posts': posts,
        'year': datetime.now().year,
    })

def blogpost(request, parametr):
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(request, 'app/blogpost.html', {
        'post_1': post_1,
        'comments': comments,
        'form': form,
        'year': datetime.now().year,
    })

def videopost(request):
    return render(request, 'app/videopost.html', {
        'title': 'Видео о поселке',
        'year': datetime.now().year,
    })