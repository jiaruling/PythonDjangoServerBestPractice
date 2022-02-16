"""
    自定义中间件
    中间件中可以定义以下 5 个方法
        process_request(self, request)
        process_response(self, request, response)
        process_view(self, request, view_func, view_args, view_kwargs)
        process_template_response(self, request, response)
        process_exception(self, request, exception)
"""
import time

from django.utils.deprecation import MiddlewareMixin

from systemConfig.models import AccessLog


# 访问日志
class AccessLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method != "GET":
            if request.META.get('HTTP_X_FORWARDED_FOR'):
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            path = request.get_full_path().split("?")
            if len(path) == 2:
                query = path[1]
            else:
                query = ""
            if request.body.decode():
                body = request.body.decode()
            else:
                body = None
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            log = AccessLog(req_url=path[0], req_method=request.method, req_query=query,
                            req_body=body, req_ip=ip, req_user=user)
            log.save()
            request.META["access_id"] = str(log.id)
            request.META["time"] = str(time.time() * 1000000)  # us

    def process_response(self, request, response):
        if request.method != "GET":
            AccessLog.objects.filter(id=int(request.META["access_id"])).update(
                resp_body=response.getvalue().decode(), resp_status_code=response.status_code,
                resp_time=time.time() * 1000000 - float(request.META["time"]))
        return response
