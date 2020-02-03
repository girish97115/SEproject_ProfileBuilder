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

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'profiles/home.html', context)

class FacultyProfileListView(ListView):
    model = FacultyProfile
    template_name = 'profiles/home.html'
    context_object_name = 'profiles'
    paginate_by = 5      

class FacultySearchList(ListView):
    model = FacultyProfile
    template_name = 'profiles/search_listview.html'
    context_object_name = 'profiles'
    paginate_by = 5    


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users_list = User.objects.filter(username__icontains=query)
            object_list = FacultyProfile.objects.none()
            for users in users_list:
                object_list = object_list.union(FacultyProfile.objects.filter(user = users))
        else:
            object_list = FacultyProfile.objects.all()  
        return object_list    

def bookmark_profile(request, id):
    profile = get_object_or_404(FacultyProfile, id = id)
    if profile.bookmark.filter(id = request.user.id).exists():
        post.bookmark.remove(request.user)
    else:
        post.bookmark.add(request.user)    
    return HttpResponseRedirect(home)
        
def FacultyInfo(request):
    return render(request, 'profiles/facultyinfo.html')