# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Vimeouser 
def search_user(request):
    return render_to_response('vimeo_user_search.html',locals(),context_instance = RequestContext( request ) )

def ajax_user_list(request):
    user_list=Vimeouser.objects.filter(name__istartswith=request.GET['name'])
    if(request.GET.get('filter') and request.GET['filter']!='all'):
        user_list=user_list.filter(**{request.GET['filter']:True})
    return render_to_response('ajax_user_list.html',locals(),context_instance = RequestContext( request ),)