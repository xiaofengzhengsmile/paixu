from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^data/$', views.data.as_view(), name='data'),
]