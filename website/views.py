__author__ = 'episage'

from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name = "base.html"