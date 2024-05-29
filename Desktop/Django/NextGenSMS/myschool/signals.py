from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import StaffProfile

@receiver(post_save, sender=User)
def create_or_update_staff_profile(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(
            user=instance, 
            years_of_service=0,  # Corrected field name
            salary=0.0  # Added salary field initialization
        )
    else:
        if hasattr(instance, 'staffprofile'):
            instance.staffprofile.save()
        else:
            StaffProfile.objects.create(
                user=instance, 
                years_of_service=0,  # Corrected field name
                salary=0.0  # Added salary field initialization
            )
