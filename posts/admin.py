from django.contrib import admin
from posts.models import Post

# Register your models here.


# Decorator approach
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'published_date'] # all are the fields same as of Post Model shown on admin interface
    list_display_links = ['id', 'post_title'] # display as link on admin interface
    list_filter = ['published_date']  # display filter on admin interface on field published date
    search_fields = ['post_title'] # display search box, searches on post_title

# admin.site.register(Post, PostAdmin) # Need to register PostAdmin (ModelAdmin) along with Post Model
