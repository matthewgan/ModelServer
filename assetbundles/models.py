from django.db import models
from django.conf import settings
from categories.models import Category


class AssetBundle(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="模型名称")
    category = models.ForeignKey(Category,
                                 verbose_name="所属类别",
                                 related_name='asset_bundle',
                                 on_delete=models.SET_NULL,
                                 null=True)
    fetchUrl = models.CharField(max_length=200,
                                verbose_name="下载地址")
    thumbnail = models.CharField(max_length=200,
                                 verbose_name="缩略图",
                                 null=True,
                                 blank=True)
    description = models.CharField(max_length=500,
                                   verbose_name="描述",
                                   blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='asset_bundle',
                              verbose_name="拥有者",
                              on_delete=models.SET_NULL,
                              null=True)
    isPublic = models.BooleanField(default=False, verbose_name="是否公开")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.isPublic = self.category.isPublic
        super(AssetBundle, self).save()

    class Meta:
        verbose_name = "素材模型"
        verbose_name_plural = "素材模型"
