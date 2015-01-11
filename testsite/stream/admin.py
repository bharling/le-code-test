from django.contrib import admin

from models import Stream


class StreamAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'tweet', 'photo']

admin.site.register(Stream, StreamAdmin)
