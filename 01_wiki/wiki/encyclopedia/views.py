from django.http import HttpResponse
from django.shortcuts import render
from markdown2 import Markdown
from . import util

markdowner = Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, name):
    entryInfo = util.get_entry(name)
    entryInfo_converted = None
    isEmpty = entryInfo == None
    if(not isEmpty):
        entryInfo_converted = markdowner.convert(entryInfo)
    else:
        entryInfo_converted = None
    
    return render(request, "encyclopedia/entryPage.html", {
        "title": name,
        "entryInfo": entryInfo_converted,
        "isEmpty": entryInfo == None
    })
