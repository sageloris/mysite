from django.db import models


# Create your models here.
class MysiteSystem(models.Model):
    sys_name = models.CharField(max_length=32, unique=True, verbose_name="系统名称")
    sys_title = models.CharField(max_length=32, verbose_name="系统标题")
    sys_url = models.CharField(max_length=128, verbose_name="系统连接")

    class Meta:
        verbose_name = '系统'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return super().__str__()


class WebsiteInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name="网站标题")
    logo = models.CharField(max_length=128, verbose_name="网站logo")
    author = models.CharField(max_length=32, verbose_name="站长")


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return super().__str__()
