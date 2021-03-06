from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(verbose_name="类别名称",
                            max_length=50)
    isPublic = models.BooleanField(verbose_name="是否公开",
                                   default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name="拥有者",
                              related_name='category',
                              on_delete=models.SET_NULL,
                              null=True,
                              )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"
