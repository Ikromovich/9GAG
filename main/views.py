from django.shortcuts import render, redirect
from main.models import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

def index(request):

    return render(request, "main/index.html")



class UploadPost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['category','comment','file']
    template_name = "layouts/form.html"
    success_url = reverse_lazy("main:upload")

    def setup (self,request,*args,**kwargs):
        super().setup(request,*args,**kwargs)

        request.title = _("Yuklash")

    def form_valid(self,form):
        messages.success(self.request,_("Muvaffaqqiyatli qo'shildi."))
        return super().form_valid(form)