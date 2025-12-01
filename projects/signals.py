# projects/signals.py
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """
    يضمن إن كل يوزر عنده بروفايل، سواء كان جديد أو قديم
    """
    Profile.objects.get_or_create(user=instance)
    print(f"Profile ensured for {instance.username}")  # اختياري، احذفه بعدين