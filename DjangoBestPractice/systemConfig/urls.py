from django.urls import path, include

from . import views
# 反向解析路由这一行不能少
app_name = "system_config"

urlpatterns = [
    path("health/", views.health, name="health"),

]
