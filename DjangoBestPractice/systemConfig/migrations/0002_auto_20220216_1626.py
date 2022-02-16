# Generated by Django 2.2 on 2022-02-16 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemConfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='req_body',
            field=models.TextField(help_text='请求body', null=True, verbose_name='请求body'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='req_ip',
            field=models.CharField(help_text='请求IP', max_length=32, null=True, verbose_name='请求IP'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='req_method',
            field=models.CharField(help_text='请求方式', max_length=8, null=True, verbose_name='请求方式'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='req_query',
            field=models.TextField(help_text='请求参数', null=True, verbose_name='请求参数'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='req_url',
            field=models.URLField(help_text='请求url', null=True, verbose_name='请求url'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='req_user',
            field=models.ForeignKey(help_text='访问者', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='访问者'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='resp_body',
            field=models.TextField(help_text='响应body', null=True, verbose_name='响应body'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='resp_status_code',
            field=models.SmallIntegerField(help_text='响应状态码', null=True, verbose_name='响应状态码'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='resp_time',
            field=models.IntegerField(help_text='请求耗时', null=True, verbose_name='请求耗时'),
        ),
    ]
