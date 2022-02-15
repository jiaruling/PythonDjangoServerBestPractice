from django.apps import AppConfig


class SystemConfigConfig(AppConfig):
    name = 'systemConfig'

    # verbose_name指定在admin管理界面中显示的名称
    # verbose_name_plural指定在admin管理界面中显示的复数名称
    verbose_name = "系统配置"
    verbose_name_plural = verbose_name
