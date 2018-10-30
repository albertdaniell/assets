from django.conf.urls import url
from . import views

import operator
from .views import (DepartmentListView,
DepartmentCreateView,
DepartmentCreateView,
DepartmentUpdateView,
DepartmentDetailView,
DepartmentDeleteView,
DepartmentSearchListView)


urlpatterns = [

    
  
    url(r'home',DepartmentListView.as_view(),name='all-departments'),
    url('new/',DepartmentCreateView.as_view(),name='department-create'),
    url('search/',views.search,name='search-departments'),
    url('(?P<pk>\d+)/$', DepartmentDetailView.as_view(), name='department-detail'),
    url('(?P<pk>\d+)/update',DepartmentUpdateView.as_view(),name='department-update'),
    url('(?P<pk>\d+)/delete', DepartmentDeleteView.as_view(), name='department-delete'),
    
 

   
]
