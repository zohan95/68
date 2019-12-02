import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_add(request, *args, **kwargs):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = int(request_data['A'])
    b = int(request_data['B'])
    data = {
        'answer': a + b
    }
    return JsonResponse(data)


@csrf_exempt
def api_sub(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = int(request_data['A'])
    b = int(request_data['B'])
    data = {
        'answer': a - b
    }
    return JsonResponse(data)


@csrf_exempt
def api_mult(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = int(request_data['A'])
    b = int(request_data['B'])
    data = {
        'answer': a * b
    }
    return JsonResponse(data)


@csrf_exempt
def api_div(request):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    a = int(request_data['A'])
    b = int(request_data['B'])
    if b==0:
        data = {
            'Error': "Division by zero!"
        }
    else:
        data = {
            'answer': a / b
        }
    return JsonResponse(data)


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

