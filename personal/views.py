from django.shortcuts import render
from django.views.generic import TemplateView

class PersonalView(TemplateView):
    template_name = 'personal/home.html'
