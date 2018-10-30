# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# import flash messages

from django.contrib import messages

# Import department model
from .models import AssetManager

# Import class based views

from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)


# Create your views here.


def index(request):
    
    return render(request,'assetmanager/index.html')


class AssetListView(ListView):
    model=AssetManager
    context_object_name='assets'
    template_name='assetmanager/index.html'
    ordering='-date_added'
    paginate_by=20

class AssetCreateView(CreateView):
    model=AssetManager
    fields=['asset_serial_number','asset_name','asset_brand','asset_specification','department_assigned']
    def form_valid(self, form):
        form.instance.assignee = self.request.user
        messages.success(self.request, "Asset added")
        return super(AssetCreateView,self).form_valid(form)
        return redirect('asset-index')
  

class AssetDetailView(DetailView):
    model=AssetManager
   

class AssetUpdateView(UpdateView):
    model=AssetManager
    fields=['asset_serial_number','asset_name','asset_brand','asset_specification','department_assigned']
    

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(self.request, "Asset Updated")
        return super(AssetUpdateView,self).form_valid(form)
        
        
        return redirect('asset-index')

class AssetDeleteView(DeleteView):
    model=AssetManager
    
    success_url='../home/'  
