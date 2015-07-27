__author__ = 'v-zhuan'

from PicShip.service import user_service
from django.http import HttpResponse

def login(request) :
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    if (user_service.login(user_name, password))
        return HttpResponse("login OK");