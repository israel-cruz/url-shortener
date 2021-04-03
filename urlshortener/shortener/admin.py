from django.contrib import admin
from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('link', 'uuid', 'created')
    readonly_fields = ('uuid','created',)

admin.site.register(Url, UrlAdmin)