from django.conf.urls import url
from . import views
from .views import (AssetnameListView,AssetnameCreateView, AssetnameDetailView)

import operator


urlpatterns = [
 
    # url(r'home',views.index,name='assetname-index'),
    url(r'home',AssetnameListView.as_view(),name='assetname-index'),
    url('new/',AssetnameCreateView.as_view(),name='assetname-create'),
    url('(?P<pk>\d+)/$', AssetnameDetailView.as_view(), name='assetname-detail'),
      
]

