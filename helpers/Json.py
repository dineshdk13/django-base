from django.shortcuts import HttpResponse
import json, codecs


def successResponse(message,data=None,http_code=200,json_format=True):

    response = {
        "status": "OK",
        "message":message,
        "data": data,
        "http_code":http_code
    }
    if json_format:
        response = json.dumps(response)

    return HttpResponse(response, content_type='Application/json', status=int(http_code))

def errorResponse(message,http_code=401,json_format=True):

    response = {
        "status": "ERROR",
        "message":message,
        "data": None,
        "http_code":http_code
    }
    if json_format:
        response = json.dumps(response)

    return HttpResponse(response, content_type='Application/json', status=int(http_code))
