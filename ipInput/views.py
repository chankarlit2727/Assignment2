import requests
from .models import Link
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def index(request):
    return render(request, 'ipInput/home.html')

def getLink(request):
    queryset = Link.objects.all()[:10]
    return JsonResponse({"link":list(queryset.values())})
 
    
class CreateLink(CreateView):
    model = Link
    fields=['link_name', 'link_text', 'link_status_code']

    def form_valid(self, form):
        try:
            link_text = form.instance.link_text
            link_ip_address= requests.get(link_text, auth=('admin', 'Puw5uTru'), verify=False)
            status = link_ip_address.status_code
            print(status)
            if status == 200:
                form.instance.link_status_code = True
                form.save()   
                return super().form_valid(form)
        except:
            form.instance.link_status_code = False
            form.save()
            return super().form_valid(form)
            

class UpdateLink(UpdateView):
    model = Link
    fields=['link_name', 'link_text', 'link_status_code']

    def form_valid(self, form):
        try:
            link_text = form.instance.link_text
            link_ip_address= requests.get(link_text, auth=('admin', 'Puw5uTru'), verify=False)
            status = link_ip_address.status_code
            if status == 200:
                form.instance.link_status_code = True
                form.save()
                
            return super().form_valid(form)
        except:
            form.instance.link_status_code = False
            form.save()
            return super().form_valid(form)

class DeleteLink(DeleteView):
    model = Link
    success_url=reverse_lazy('index')