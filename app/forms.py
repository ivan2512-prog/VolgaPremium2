from django import forms
from .models import Comment

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя", 
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="E-mail", 
        required=False, 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        label="Возраст", 
        required=False, 
        min_value=18, 
        max_value=99,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    rating = forms.ChoiceField(
        label="Оцените поселок (от 1 до 5)",
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        widget=forms.RadioSelect
    )
    liked_land = forms.BooleanField(label="Участки", required=False)
    liked_nature = forms.BooleanField(label="Природа и Волга", required=False)
    liked_infra = forms.BooleanField(label="Инфраструктура", required=False)
    
    interest = forms.ChoiceField(
        label="Что вас интересует?",
        choices=[
            ('uchastok', 'Покупка участка'),
            ('dom', 'Строительство дома'),
            ('consult', 'Консультация'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label="Ваши пожелания",
        required=False,
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    # Импортируем стандартную форму входа из Django
from django.contrib.auth.forms import AuthenticationForm

# Создаем нашу форму входа на основе стандартной, добавляя классы Bootstrap
class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем стили Bootstrap к полям
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        
        # Переводим названия на русский
        self.fields['username'].label = "Имя пользователя"
        self.fields['password'].label = "Пароль"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Ваш комментарий"}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }