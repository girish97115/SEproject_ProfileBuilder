from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from profiles.models import StudentProfile, FacultyProfile
from ckeditor.widgets import CKEditorWidget
User = get_user_model()
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email','is_teacher' ,'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['image', 'about']

class FacultyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        about = forms.CharField(widget= CKEditorWidget(), label = "body")
        articles = forms.CharField(widget= CKEditorWidget(), label = "body")
        projects = forms.CharField(widget= CKEditorWidget(), label = "body")
        fields = ['image', 'about', 'articles', 'projects']