from django.contrib import admin
from.models import Post
from django_summernote.admin import SummernoteModelAdmin






class BlogSummernote(SummernoteModelAdmin):
    summer_note_fields = ('text_min', 'body')
    list_display = ('title','slug', 'author', 'published', 'status', 'image')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')

admin.site.register(Post, BlogSummernote)



