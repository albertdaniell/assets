# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404   
from .models import Assetname
from assetmanager.models import AssetManager
from department.models import Department

import operator



# import flash messages

from django.contrib import messages


# Import class based views

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.


def index(request):
    
    return render(request,'assetname/index.html')

class AssetnameListView(ListView):
    model=Assetname
    template_name='assetname/index.html'
    context_object_name='assetname'
    
    paginate_by=8

class AssetnameCreateView(CreateView):
    model=Assetname
    fields=['asset_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Asset Created Successfully")
        return super(AssetnameCreateView,self).form_valid(form)
        
        return redirect('assetname-index')

class AssetnameDetailView(DetailView):
    model=Assetname
  

    def get_context_data(self,**kwargs):
        # Get pk of asset from the url
        assetname=Assetname.objects.get(pk=self.kwargs.get('pk'))
        assets = AssetManager.objects.filter(asset_name=assetname)

        # map the assets that have been assigned to the department

        department = Department.objects.all()
        depass= AssetManager.objects.filter(asset_name=assetname).distinct()
        context ={
            # 'department':department,
            'assets':assets,
            'assetname':assetname,
            'depass':depass
        }

        return context
    
    
