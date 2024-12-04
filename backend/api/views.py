from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    print(request.GET['abc'])
    print(data)
    data['params'] = dict(request.GET)
    data['content-type'] = request.content_type
    return JsonResponse(data)