from django.db import models
from django.contrib.auth.models import User


class Fbx(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="名称")
    fetchUrl = models.URLField(max_length=200,
                               verbose_name="下载地址")
    owner = models.ForeignKey(User, verbose_name="拥有者",
                              related_name='fbx',
                              on_delete=models.SET_NULL,
                              null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "FBX文件"
        verbose_name_plural = "FBX文件"
