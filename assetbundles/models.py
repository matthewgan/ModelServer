from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class AssetBundle(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="模型名称")
    category = models.ForeignKey(Category,
                                 verbose_name="所属类别",
                                 related_name='asset_bundle',
                                 on_delete=models.SET_NULL,
                                 null=True)
    fetchUrl = models.URLField(max_length=200,
                               verbose_name="下载地址")
    thumbnail = models.URLField(max_length=200,
                                verbose_name="缩略图",
                                null=True,
                                blank=True)
    description = models.CharField(max_length=500,
                                   verbose_name="描述",
                                   blank=True)
    owner = models.ForeignKey(User, related_name='asset_bundle',
                              verbose_name="拥有者",
                              on_delete=models.CASCADE,
                              editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "素材模型"
        verbose_name_plural = "素材模型"
