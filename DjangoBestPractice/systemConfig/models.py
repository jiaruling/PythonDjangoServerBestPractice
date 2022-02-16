import uuid
import time

from django.db import models
from django.contrib.auth.models import User


class CIA(models.Model):
    # 显示的设置主键【不写这一行代码，Django也会隐式的设置主键】
    id = models.AutoField(primary_key=True, verbose_name="id", help_text="id")

    class Meta:
        abstract = True  # 指定是抽象类


class CIB(models.Model):
    # UID【不允许为空且唯一】
    uid = models.CharField(max_length=128, default=uuid.uuid4, unique=True, verbose_name="uid", help_text="uid")

    class Meta:
        abstract = True  # 指定是抽象类


class CIC(models.Model):
    # 创建时间
    created_at = models.IntegerField(default=time.time(), verbose_name="创建时间", help_text="创建时间")

    class Meta:
        abstract = True  # 指定是抽象类


class CID(models.Model):
    # 更新时间
    updated_at = models.IntegerField(default=time.time(), verbose_name="最后更新时间", help_text="最后更新时间")

    class Meta:
        abstract = True  # 指定是抽象类


class CIE(models.Model):
    # 逻辑删除
    deleted_at = models.IntegerField(null=True, verbose_name="逻辑删除", help_text="逻辑删除")

    class Meta:
        abstract = True  # 指定是抽象类


class CIF(models.Model):
    # 备注【允许为空】
    remark = models.CharField(max_length=256, null=True, verbose_name="备注", help_text="备注")

    class Meta:
        abstract = True  # 指定是抽象类


class CIG(models.Model):
    # 创建者
    create_user = models.ForeignKey(to=User, on_delete=models.SET_NULL, verbose_name="创建者", null=True, blank=True)

    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoA(CIA, CIB, CIC, CID, CIE, CIF, CIG):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoB(CIA, CIC, CID, CIE, CIF, CIG):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoC(CIA, CIC, CID, CIE, CIF):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoD(CIA, CIC, CID, CIE):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoE(CIA, CIC, CID):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoF(CIA, CIC):
    class Meta:
        abstract = True  # 指定是抽象类


class CommonInfoG(CIA):
    class Meta:
        abstract = True  # 指定是抽象类


class AccessLog(CommonInfoF):
    req_url = models.URLField(null=True, verbose_name="请求url", help_text="请求url")
    req_method = models.CharField(null=True, max_length=8, verbose_name="请求方式", help_text="请求方式")
    req_query = models.TextField(null=True, verbose_name="请求参数", help_text="请求参数")
    req_body = models.TextField(null=True, verbose_name="请求body", help_text="请求body")
    req_ip = models.CharField(null=True, max_length=32, verbose_name="请求IP", help_text="请求IP")
    req_user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name="访问者", help_text="访问者")
    resp_body = models.TextField(null=True, verbose_name="响应body", help_text="响应body")
    resp_status_code = models.SmallIntegerField(null=True,verbose_name="响应状态码", help_text="响应状态码")
    resp_time = models.IntegerField(null=True, verbose_name="请求耗时", help_text="请求耗时")

    class Meta:
        db_table = "access_log"
        verbose_name = "访问日志"
        verbose_name_plural = verbose_name

