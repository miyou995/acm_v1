from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DetailView
from pprint import pprint
from .forms import WilayaForm, CommuneForm 
from location.models import Wilaya, Commune 
# Create your views here.
##### a deplacer dans location views
class WilayaView(CreateView):
    template_name= "add-wilaya.html"
    form_class= WilayaForm
    model = Wilaya 
    success_url = reverse_lazy('order:addwilaya')

    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
class CommuneView(CreateView):
    template_name= "add-commune.html"
    form_class= CommuneForm
    model = Commune 
    success_url = reverse_lazy('order:addcommune')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(CommuneView, self).get_context_data(**kwargs)
        context["wilayas"] = Wilaya.objects.all()
        return context 