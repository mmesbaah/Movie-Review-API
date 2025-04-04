from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('movie_title', 'user__username', 'content')
    readonly_fields = ('created_at', 'updated_at')
