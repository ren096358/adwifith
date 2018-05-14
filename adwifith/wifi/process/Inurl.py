from django.shortcuts import render
from django.http import JsonResponse
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


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
