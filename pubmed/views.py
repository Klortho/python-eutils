from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, Template

#from backend.cgi import *
from backend.cms import *
from backend.search import *
from backend.docsum import *

def dispatch(request):
    if (request.GET.get('term') == ''):
        return redirect("http://iwebdev2/staff/misiurev/dncbi/index.cgi/pubmed/")
    
    if (request.GET.get('term') != 'None'):
        return dosearch(request)

    return home(request)
        
        
def home(request):
    backend = cms("pmh")
    page = backend.get("about")
    
    if (page.status_code != 200):
        return HttpResponseNotFound("<h1>Page "+page.url+" not found</h1>")
    
    return render_to_response("pubmed/index.html", { "title": page.title, "head": page.head, "body": page.body })


def dosearch(request):
    backend = search('pubmed');
    response = backend.request('cat', { "groupBy": "PubDate" });
    
    docs = docsum('pubmed');
    response2 = docs.request(docs.extractIds(response))
    return HttpResponse(response2)
