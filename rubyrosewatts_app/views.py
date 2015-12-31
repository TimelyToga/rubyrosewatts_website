__author__ = 'Tim'

try: import simplejson as json
except ImportError: import json
from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request):
    template = loader.get_template('main.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def skills(request):
    template = loader.get_template('skills.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))