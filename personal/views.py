from django.shortcuts import render
from django.views.generic import TemplateView

from personal.admin import Portfolio

def index_view(request):

    portfolios = Portfolio.objects.all().order_by('-id')

    context = {
        'portfolios': portfolios
    }

    return render(request, 'personal/index.html', context)
