from django.contrib import admin
from .models import Post,Question,Call,Upload,Search

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display =['id','title','created_at']
	list_display_links = ['title']

@admin.register(Question)
class question_board_Admin(admin.ModelAdmin):
	list_display=['id','title','created_at']
	list_display_links = ['title']

@admin.register(Call)
class call_board_Admin(admin.ModelAdmin):
	list_display=['id','title','created_at']
	list_display_links = ['title']

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
	list_display = ['id','photo']
	list_display_links = ['id']

@admin.register(Search)
class FontAdmin(admin.ModelAdmin):
	list_display=['id', 'title']
	list_display_links = ['title']



# Register your models here.
