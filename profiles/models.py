from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from ckeditor.fields import RichTextField
User = get_user_model()
# Create your models here.
class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='staff_pics')
    about = RichTextField(max_length=1024)
    articles = RichTextField(max_length=1024, blank = True)
    projects = RichTextField(max_length=1024, blank = True)
    bookmark = models.ManyToManyField(User, related_query_name= 'bookmark',blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='student_pics')
    about = models.CharField(max_length=1024)
    def __str__(self):
        return f'{self.user.username} Profile'

class Publication(models.Model):
    facultyprofile = models.ForeignKey(FacultyProfile, related_name='publications', on_delete= models.CASCADE)
    publicationtype = models.CharField(max_length=1024, default='Unknown')
    year = models.IntegerField(default = 2020)
    title = models.CharField(max_length=1024, default='-')