# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404   

import operator



# import flash messages

from django.contrib import messages

# Import department model
from .models import Department
from assetmanager.models import AssetManager


# Import class based views

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.


def index(request):
    
    return render(request,'department/index.html')

# List based view class
class DepartmentListView(ListView):
    
    model=Department
    template_name='department/all_departments.html'
    context_object_name='departments'
    ordering='-date_created'
    paginate_by=20

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        context['alldeps'] = Department.objects.all().order_by('-date_created')
        # Add any other variables to the context here
       
        return context

class DepartmentCreateView(CreateView):
    model=Department

    

class DepartmentCreateView(CreateView):
    model=Department
    fields=['department_name','department_floor','department_head']

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(self.request, "Department Created Successfully")
        return super(DepartmentCreateView,self).form_valid(form)
        
        
        return redirect('all-departments')

class DepartmentDetailView(DetailView):
    model=Department
  

    def get_context_data(self,**kwargs):
        # Get pk of asset from the url
        department=Department.objects.get(pk=self.kwargs.get('pk'))

        # map the assets that have been assigned to the department
        assets = AssetManager.objects.filter(department_assigned=department)
        alldeps = Department.objects.all().order_by('-date_created')
        context ={
            'department':department,
            'assets':assets,
            'alldeps':alldeps,
            
        }

        return context
        
        



    # def get_context_data(self,pk, **kwargs):
      

    #     context = super(DepartmentDetailView, self).get_context_data(**kwargs)
    #     context['department'] = Department.objects.get(pk=pk)
    #     context['assets'] = AssetManager.objects.filter(department_assigned=15)
    #     return context
    
    
   

class DepartmentUpdateView(UpdateView):
    model=Department
    fields=['department_name','department_floor','department_head']
    

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(self.request, "Department Updated")
        return super(DepartmentUpdateView,self).form_valid(form)
        
        
        return redirect('all-departments')

class DepartmentDeleteView(DeleteView):
    model=Department
    
    success_url='../home/'  




class DepartmentSearchListView(DepartmentListView):
    """
    Display a Department List page filtered by the search query.
    """
    paginate_by = 10
    template_name='department/department_search.html'
    model=Department
    context_object_name='result'

    # def get_queryset(self):
    #     result= super(DepartmentSearchListView,self) .get_queryset()


#    if request.method == "POST":
#        q=request.POST['q']
#     else:
#         q=''
#     results=Department.objects.filter(department_name__contains=q)

#         return result
    
def search(request):
  
        q=request.GET['q']
        results=Department.objects.filter(department_name__contains=q)
        return render(request,'department/department_search.html',{'results':results})      
    