from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wifi.model.Hotspotsinfo import Hotspotsinfo
import pdb


@csrf_exempt
def index(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    index_page = input.get('index-page', '')
    mac = input.get('mac', '')
    link_login_only = input.get('link-login-only', '')
    routerName = input.get('server-name', '')

    if link_login_only == "../05final/final.php":
        link_login_only = "final"

    hotspot = Hotspotsinfo()
    rid = hotspot.getRid(routerName)
    if index_page == "start":
        url = hotspot.getUrl(rid, "portal")
    else:
        url = hotspot.getUrl(rid, "final")

    split = url.split("/")
    nextLink = split[2].replace(".php", "")
    data = {
        'rid': rid,
        'mac': mac,
        'link_login_only': link_login_only,
        'nextLink': nextLink,
    }
    return render(request, 'index.html', {'data': data})


def test(request):
    return render(request, 'imitationRouter.html')
