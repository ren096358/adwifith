from django.shortcuts import render
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


def adv(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac', '')
    rid = input.get('rid', '')
    link_login_only = input.get('link_login_only', '')

    hotspot = Hotspotsinfo()
    adUrl = hotspot.getAdvUrl(rid, mac)
    # pdb.set_trace()
    data = {
        'rid': rid,
        'mac': mac,
        'link_login_only': link_login_only,
        'adUrl': adUrl,
    }
    return render(request, 'adv.html', {'data': data})
