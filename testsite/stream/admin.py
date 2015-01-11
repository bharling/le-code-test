from django.contrib import admin

from models import Stream


class StreamAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'tweet', 'photo', 'deleted']
    actions=['delete_items', 'restore_items']
    
    def delete_items(self, request, queryset):
        for item in queryset:
            if item.photo:
                item.photo.deleted = True
            if item.tweet:
                item.tweet.deleted = True
            item.save()
    delete_items.short_description = "Delete selected streams"
    
    def restore_items(self, request, queryset):
        for item in queryset:
            if item.photo:
                item.photo.deleted = False
            if item.tweet:
                item.tweet.deleted = False
            item.save()
    restore_items.short_description = "Restore selected streams"

admin.site.register(Stream, StreamAdmin)
