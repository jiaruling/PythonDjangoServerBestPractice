from django.apps import AppConfig


class BaseConfigConfig(AppConfig):
    name = 'baseConfig'

    # verbose_name指定在admin管理界面中显示的名称
    # verbose_name_plural指定在admin管理界面中显示的复数名称
    verbose_name = "应用配置"
    verbose_name_plural = verbose_name
