from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'created_date', 'published_date']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
admin.site.register(Post, PostAdmin)


