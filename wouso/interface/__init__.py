import logging
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext, Context
from wouso.interface.pages.models import StaticPage

# Get a specific logger for this module
logger = logging.getLogger('interface')

def render_string(template, data=None):
    """ Provide game context render_to_string, used by widget generators """

    return render_to_string(template,
            dictionary=data)

def get_static_pages():
    """ Return a list of static pages ordered by position, for rendering in footer """
    return StaticPage.objects.filter(hidden=False).order_by('position')

def detect_mobile(request):
    if request.META.has_key("HTTP_USER_AGENT"):
        s = request.META["HTTP_USER_AGENT"].lower()
        for i in ('nokia', 'mobile'):
            if i in s:
                return True
    return False