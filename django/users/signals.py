from django.contrib.auth.models import User
from .models import Profile, Location
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, post_delete # means that post-> create, so when we create save
from django.db.models import Q

@receiver(post_save, sender=User) # link this signal with the User model so will be executed when we create a User model
def create_user_profile(sender, instance, created, **kwargs):
    """
    will be executed when User instanse is created to create a Profile instance
    - sender: the model that will invoke the signal to run which is here for an example the User
    - instance: the instance of the model that will invoke the signal
    - created: a boolean value that will let us kow if the model (User) created or not
    - **kwargs: additinol keyword argument that function have
    """
    if created: # when User model is created 
        # then create a Profile model
        Profile.objects.create(user=instance, bio="labbalhblah")


@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        #* what is this profile attribut? cause Profile model have a 1:1 relaation between it and Location model so django as default will create a location attribute inside the Profile and a profile attribute inside the Location
        #! Location.objects.create(profile=instance) this line of code will make an error 
        #^ so what is the proper way to make it? 
            # 1. by create the location 
            # 2. then append it into location attribute that inside the Profile model
            # 3. then dont forget to save it
        location = Location.objects.create()
        instance.location = location
        instance.save()

        

@receiver(pre_delete, sender=Profile)
def delete_location_when_user_deleted(sender, instance, **kwargs):
    user_id = instance.user.id
    user_location_id = Profile.objects.filter(user=user_id).values_list('location', flat=True).get()
    Location.objects.get(id=user_location_id).delete()

# another way to delete the location
@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwargs):
    if instance.location is not None: # if the profile has loaction
        isinstance.location.delete() # then delete it 