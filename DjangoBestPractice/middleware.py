"""
    自定义中间件
    中间件中可以定义以下 5 个方法
        process_request(self, request)
        process_response(self, request, response)
        process_view(self, request, view_func, view_args, view_kwargs)
        process_template_response(self, request, response)
        process_exception(self, request, exception)
"""

from django.utils.deprecation import MiddlewareMixin


# from .systemConfig.models import AccessLog

# 访问日志
class AccessLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print(ip)
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError as err:
            print(err)
        else:
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip

        # if request.method != "GET":
        #     pass
        # else:
        #     print("这是一个中间件 --> ", request.method, request.get_full_path())
        #     print("请求方式: {1}\n请求接口: {2}\n请求IP: {3}\n".format(request.method, request.get_full_path(),
        #                                                      request.META['HTTP_X_FORWARDED_FOR']))


def process_response(self, request, response):
    if request.method == "GET":
        print("这是一个中间件 --> test")
    return response
