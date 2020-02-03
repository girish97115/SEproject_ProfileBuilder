from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import FacultyProfile, StudentProfile

User = get_user_model()
@receiver(post_save, sender=User)
def create_profile(sender, instance, created ,**kwargs):
    if created:  # used to perform action only at creation time (avoid the code to execute during any update)
        if instance.is_teacher:  # access the field of instance
            profile = FacultyProfile.objects.create(user=instance) # you have correctly passed instance to foreign key and you just need to check condition for the same        

        else:
            profile = StudentProfile.objects.create(user=instance)

