from django.contrib import admin

from .models import CourseResource, Role, RoadmapStep, StepResource


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(RoadmapStep)
class RoadmapStepAdmin(admin.ModelAdmin):
    list_display = ('role', 'level', 'order', 'title')
    list_filter = ('level', 'role')
    ordering = ('role', 'level', 'order')


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'url', 'estimated_minutes')
    list_filter = ('resource_type',)


@admin.register(StepResource)
class StepResourceAdmin(admin.ModelAdmin):
    list_display = ('step', 'resource', 'is_required', 'order')
    list_filter = ('is_required',)
