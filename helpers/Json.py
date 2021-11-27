from django.shortcuts import HttpResponse
import json, codecs


def Response(data,http_code, error=True, json_format=True):
    if error:
        status = 'OK'

    else:
        status = 'ERROR'
    response = {
        "data": data,
        "status": status,
        "http_code":http_code
    }
    if json_format:
        response = json.dumps(response)

    return HttpResponse(response, content_type='Application/json', status=int(http_code))
