from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView 
)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import FacultyProfile
from search_listview.list import SearchableListView
from users.models import User
from django.urls import reverse
from users.forms import AppointmentCreationForm
from django.contrib import messages


class FacultyProfileListView(ListView):
    model = FacultyProfile
    template_name = 'profiles/home.html'
    context_object_name = 'profiles'
    paginate_by = 4


class FacultySearchList(ListView):
    model = FacultyProfile
    template_name = 'profiles/search_listview.html'
    context_object_name = 'profiles'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users_list = User.objects.filter(username__icontains=query)
            object_list = FacultyProfile.objects.none()
            for users in users_list:
                object_list = object_list.union(FacultyProfile.objects.filter(user=users))

        else:
            object_list = FacultyProfile.objects.all()

        for post in object_list:
            if post.bookmark.filter(id=self.request.user.id).exists():
                post.is_favourite = True
            else:
                post.is_favourite = False
        return object_list    


def bookmark_profile(request, pk):
    profile = get_object_or_404(FacultyProfile, id=pk)
    if profile.bookmark.filter(id=request.user.id).exists():
        profile.bookmark.remove(request.user)
    else:
        profile.bookmark.add(request.user)
    return HttpResponseRedirect(reverse('home'))


def make_appointment(request, pk):
    faculty = get_object_or_404(FacultyProfile, id=pk)
    student = request.user.studentprofile
    if request.method == "POST":
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.faculty = faculty
            appointment.student = student
            appointment.save()
            messages.success(request, f'Your Account has been updated!')
            return HttpResponseRedirect(reverse('home'))

    else:
        form = AppointmentCreationForm()

    return render(request, 'profiles/appointment.html', {'faculty': faculty, 'student': student, 'form':form})


def faculty_info(request, pk):
    profile = get_object_or_404(FacultyProfile, id=pk)
    return render(request, 'profiles/facultyinfo.html', {'profile': profile})


class BookmarksListView(ListView, LoginRequiredMixin):
    model = FacultyProfile
    template_name = 'users/bookmarks.html'
    context_object_name = 'profiles'
    paginate_by = 3

    def get_queryset(self):
        profiles = FacultyProfile.objects.all()
        object_list = []
        for profile in profiles:
            if profile.bookmark.filter(id=self.request.user.id).exists():
                object_list.append(profile)

        return object_list
