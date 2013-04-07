# Create your views here.
from  settings import SOLR_URL
from django.template.context import RequestContext
from django.shortcuts import render_to_response
import json
import urllib2 
def ajax_list(request):
    input_data=request.GET.get('text')
    if request.method=='GET' and input_data:
        data=input_data.split()
        query_data='+'.join(['*%s*' % each for each in data])
        url='%sselect?q=%s&start=0&rows=300000&wt=json&indent=true&hl=true&hl.simple.pre=<em>&hl.simple.post=</em>&hl.q=%s&hl.fragsize=0'% (SOLR_URL,query_data,query_data)
        res=urllib2.urlopen(url).read()
        res=json.loads(res)
        total=res['response']['numFound']
        result=res['response']['docs']
        i=0
        while i<total:
            result[i]['path']=res['highlighting'][result[i]['path']]['path'][0]
            i+=1
        return render_to_response('ajax_list.html',locals())