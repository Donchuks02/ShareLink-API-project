from django.contrib import admin
from .models import Content
# Register your models here.


class ContentAdmin(admin.ModelAdmin):
  list_display = ('body', 'owner')

admin.site.register(Content, ContentAdmin)