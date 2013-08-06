from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, Template

#from backend.cgi import *
from backend.cms import *
from backend.search import *
from backend.docsum import *

def dispatch(request):
    term = request.GET.get('term', '__null__')

    # Term present but is empty    
    if (term == ''):
        # Redirect to home page
        return redirect(request.path)
    
    # Term present and is not empty
    if (term != '__null__'):
        # Run search
        return dosearch(request)

    # Show landing page
    return home(request)
        
        
def home(request):
    backend = cms("paf-dev")
    page = backend.get("beer")
    
    if (page.status_code != 200):
        return HttpResponseNotFound("<h1>Page "+page.url+" not found</h1>")
    
    return render_to_response("pubmed/index.html", { "title": page.title, "head": page.head, "body": page.body })


def dosearch(request):
    backend = search('pubmed');
    response = backend.request('cat', { "groupBy": "PubDate" });
    
    docs = docsum('pubmed');
    response2 = docs.request(docs.extractIds(response))
    return HttpResponse(response2)
