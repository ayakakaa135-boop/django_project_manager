# projects/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Project, Task
from django.db.models import Count


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'status', 'created_at', 'tasks_count')
    list_filter = ('status', 'category', 'created_at', 'owner')
    search_fields = ('name', 'description')
    readonly_fields = ('tasks_count',)

    def get_queryset(self, request):
        """نحسب عدد المهام لكل مشروع مرة واحدة بكفاءة"""
        return super().get_queryset(request).annotate(
            tasks_count=Count('task')
        )

    def tasks_count(self, obj):
        """نعرض العدد في العمود"""
        return obj.tasks_count


    tasks_count.short_description = _("Number of Tasks")
    tasks_count.admin_order_field = 'tasks_count'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'completed', 'due_date', 'priority', 'creator')
    list_filter = ('completed', 'priority', 'due_date', 'project__category')
    search_fields = ('title', 'description', 'project__name')
    raw_id_fields = ('project',)