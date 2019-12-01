import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_add(request, *args, **kwargs):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = request_data['A']
    b = request_data['B']
    data = {
        'answer': a + b
    }
    return JsonResponse(data)


@csrf_exempt
def api_sub(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = request_data['A']
    b = request_data['B']
    data = {
        'answer': a - b
    }
    return JsonResponse(data)


@csrf_exempt
def api_mult(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = request_data['A']
    b = request_data['B']
    data = {
        'answer': a * b
    }
    return JsonResponse(data)


@csrf_exempt
def api_div(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = request_data['A']
    b = request_data['B']
    data = {
        'answer': a / b
    }
    return JsonResponse(data)