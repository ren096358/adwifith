from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wifi.models import *
import pdb


@csrf_exempt
def index(request):
    if request.method == 'POST':
        input = request.POST
    else:
        input = request.GET

    server_name = input.get('server-name', '')
    index_page = input.get('index-page', '')

    sql =


    sql = "select rid from forciblyprocess where routerName = '%s'" % \
          (server_name)

    if index_page == "start":
        nextUrl =
    else:
        nextUrl =
    pdb.set_trace()


def test(request):
    return render(request, 'imitationRouter.html')
