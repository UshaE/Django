from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
urlpatterns =[
path('login',views.login,name='login'),
path('footer',views.footer,name = 'footer'),
]



