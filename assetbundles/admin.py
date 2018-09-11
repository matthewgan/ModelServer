from django.contrib import admin
from .models import AssetBundle


class AssetBundleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'fetchUrl', 'thumbnail', 'owner', )
    search_fields = ('name', )


admin.site.register(AssetBundle, AssetBundleAdmin)
