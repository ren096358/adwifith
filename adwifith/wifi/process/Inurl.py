from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


@csrf_exempt
def inurl(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac_', '')
    rid = input.get('rid', '')
    url = input.get('url', '')

    hotspot = Hotspotsinfo()
    result = hotspot.insertADVR(rid, mac, url)
    data = {
        'result': result
    }
    return JsonResponse(data)
