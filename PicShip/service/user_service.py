__author__ = 'v-zhuan'

from PicShip.models import *

def login(user_name, password) :
    user = User.objects.filter(user_name = user_name, password = password)
    if user == None :
        return False
    return True
