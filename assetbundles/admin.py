from django.contrib import admin
from .models import AssetBundle


class AssetBundleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'fetchUrl', 'thumbnail', 'isPublic', 'owner', )
    search_fields = ('name', )


admin.site.register(AssetBundle, AssetBundleAdmin)
