from django.contrib import admin
from .models import Tag, Author, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter=("title", "tags", "author")
    list_display=("title", "date", "author")
    prepopulated_fields={"slug":("title",)}

    
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)