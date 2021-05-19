from django.contrib import admin
from .models import Sistema, Link 
from django.utils.html import format_html

class AdminLink(admin.ModelAdmin):
    list_display = ("nombre", "sistema", "link")

    def link(self, obj):
        return format_html("<a href={}>{}</a>", obj.enlace, obj.enlace)

admin.site.register(Link, AdminLink)
admin.site.register(Sistema)