# projects/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import os


# --- كيان التصنيف ---
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Owner"),
        # default=1

    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


# --- كيان المشروع ---
class Project(models.Model):
    STATUS_CHOICES = (
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('on_hold', _('On Hold')),
    )
    name = models.CharField(max_length=200, verbose_name=_("Project Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Owner"),
        default=1
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Category"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name=_("Status"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name



class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', _('Low')),
        ('medium', _('Medium')),
        ('high', _('High')),
    )
    title = models.CharField(max_length=200, verbose_name=_("Task Title"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', verbose_name=_("Project"))
    completed = models.BooleanField(default=False, verbose_name=_("Completed"))
    due_date = models.DateField(null=True, blank=True, verbose_name=_("Due Date"))
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name=_("Priority"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))


    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_tasks',
        verbose_name=_("Creator")
    )

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.title


def get_profile_image_path(instance, filename):
    return os.path.join('profile_images', str(instance.user.id), filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    image = models.ImageField(default='profile_images/default.png', upload_to=get_profile_image_path,
                              verbose_name="profile photo")

    def __str__(self):
        return f'{self.user.username} Profile'