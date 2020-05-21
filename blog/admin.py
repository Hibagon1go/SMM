from django.contrib import admin
from .models import Blog
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Blog, BlogAdmin)