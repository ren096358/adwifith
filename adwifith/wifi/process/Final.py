from django.shortcuts import render
from django.http import JsonResponse
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


def final(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac', '')
    rid = input.get('rid', '')
    #pdb.set_trace()
    hotspot = Hotspotsinfo()
    finalurl = hotspot.selectADVR(rid, mac)
    if rid == 336:
        finalurl = 'http://adwifi.in.th'

    data = {
        'finalurl': finalurl
    }
    return render(request, 'final.html', {'data': data})
