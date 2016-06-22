from django.contrib import admin
from .models import Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'created_date', 'published_date']
    list_display = [
        'title',
        'author',
        'created_date',
        'published_date',
        'published',
    ]

    list_filter = [
        'created_date',
        'published_date',
        'published',
    ]

    search_fields = [
        'title'
    ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        return Post.objects.filter(author=request.user)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:core_post_changelist'))

        return super(PostAdmin, self).change_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:core_post_changelist'))

        return super(PostAdmin, self).delete_view(request, object_id, extra_context)

    def history_view(self, request, object_id, extra_context=None):
        if not self.get_queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:core_post_changelist'))

        return super(PostAdmin, self).history_view(request, object_id, extra_context)
admin.site.register(Post, PostAdmin)


