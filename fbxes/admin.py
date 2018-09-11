from django.contrib import admin
from .models import Fbx


class FbxAdmin(admin.ModelAdmin):
    list_display = ('name', 'fetchUrl', 'created', 'updated')
    search_fields = ('name', )


admin.site.register(Fbx, FbxAdmin)
