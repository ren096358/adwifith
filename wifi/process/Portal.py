from django.shortcuts import render
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


def portal(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    mac = input.get('mac', '')
    rid = input.get('rid', '')
    link_login_only = input.get('link_login_only', '')

    hotspot = Hotspotsinfo()
    portalPic = hotspot.getPortalPic(rid)

    url = hotspot.getUrl(rid, "advouter")
    split = url.split("/")
    advLink = split[2].replace(".php", "")
    data = {
        'rid': rid,
        'mac': mac,
        'link_login_only': link_login_only,
        'portalPic': portalPic,
        'advLink': advLink,
    }
    # pdb.set_trace()
    return render(request, 'portal.html', {'data': data})
