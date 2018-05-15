from django.shortcuts import render
from django.http import JsonResponse
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


def inurl(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac', '')
    rid = input.get('rid', '')
    url = input.get('url', '')
    link_login_only = input.get('link_login_only', '')

    hotspot = Hotspotsinfo()
    result = hotspot.insertADVR(rid, mac, url)

    data = {
        'mac': mac,
        'rid': rid,
        'link_login_only': link_login_only
    }
    return render(request, 'inurl.html', {'data': data})
