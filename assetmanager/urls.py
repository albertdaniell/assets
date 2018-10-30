from django.conf.urls import url,include
from . import views
from .views import AssetListView,AssetCreateView,AssetDeleteView,AssetDetailView,AssetUpdateView



urlpatterns = [

   
    url(r'home', AssetListView.as_view(),name='asset-index'),
    url('new/',AssetCreateView.as_view(),name='asset-create'),
    url('(?P<pk>\d+)/$', AssetDetailView.as_view(), name='asset-detail'),
    url('(?P<pk>\d+)/update',AssetUpdateView.as_view(),name='asset-update'),
    url('(?P<pk>\d+)/delete', AssetDeleteView.as_view(), name='asset-delete'),

  

   
]
