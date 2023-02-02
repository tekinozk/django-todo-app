from django.contrib import admin

from .models import Todo,Category,Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
        "pk",
    ]

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active",
        "created_at",
        "updated_at",
        "category",
        "pk",
    ]
admin.site.register(Todo,TodoAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
