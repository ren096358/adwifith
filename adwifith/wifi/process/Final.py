from django.shortcuts import render
from django.http import JsonResponse
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


def final(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac_', '')
    rid = input.get('rid', '')

    hotspot = Hotspotsinfo()
    advurl = hotspot.selectADVR(rid, mac)
    if rid == 336:
        advurl = 'http://adwifi.in.th'

    data = {
        'advurl': advurl
    }
    return render(request, 'final.html', {'data': data})
