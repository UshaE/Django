from django.shortcuts import render
from AdminPanel.Models import models
from django.http import HttpResponse
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from AdminPanel.Models import models
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
'''
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s: %(message)s')
filehandler = logging.FileHandler('test.log')
filehandler.setFormatter(formatter)

logger.addHandler(filehandler) '''

#
'''logging.basicConfig(filename='../logs/request.log',level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')'''

# here you can also add some local logger should you want: to stdout with streamhandler, or to a local file...
'''
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        ud = models.Users.objects.get(username='request.data[username]')
        username = ud.username
    return Response(username)
'''


# Create your views here.
def login(request):
    # ob = models.UserDetails(username='krishnakr',password='123',email='kr@gmail.com')
    # ob.save()
    ''' rs = models.UserDetails.objects.all()
     res = 'Testing results'
     for elt in rs:
         res += elt.username + "<br>" + elt.password + "<br>" + elt.email + "<br>"
 '''
    # return HttpResponse(res)
    logger.debug(request)
    return render(request,'login.html')

def footer(request):
    return render(request,'footer.html')
