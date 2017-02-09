from django.contrib import admin
from .models import Post

# Define the column display.
class PostAdmin(admin.ModelAdmin):
	list_display=['author','title','text','created_date','published_date']
	
# Register your models here.
admin.site.register(Post, PostAdmin)
