from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def health(request):
    return JsonResponse({"code": 200, "msg": "健康检查", "data": None})
