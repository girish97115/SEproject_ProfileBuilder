from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, StudentProfileUpdateForm, FacultyProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}! You are now able to login')
            return redirect('/')
    else:
        form = CustomUserCreationForm()   
    return(render(request, 'users/register.html',{'form':form}))

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.is_teacher:
            p_form = FacultyProfileUpdateForm(request.POST,request.FILES,instance=request.user.facultyprofile)
        else:
            p_form = StudentProfileUpdateForm(request.POST,request.FILES,instance=request.user.studentprofile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.is_teacher:
            p_form = FacultyProfileUpdateForm(instance=request.user.facultyprofile)
        else:
            p_form = StudentProfileUpdateForm(instance=request.user.studentprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)     

