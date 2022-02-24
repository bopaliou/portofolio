from django.contrib import admin
from blog.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'last_modified')
    list_filter = ('created_at',)
    search_fields = ('title', 'body')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
