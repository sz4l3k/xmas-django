from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from diamenty import views

urlpatterns = [
    path('', views.index, name='index'),
    path('onlogin', views.onlogin, name='onlogin')
] + staticfiles_urlpatterns()

