from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request, name):
    entryInfo = util.get_entry(name)

    return render(request, "encyclopedia/entryPage.html", {
        "title": name,
        "entryInfo": entryInfo,
        "isEmpty": entryInfo == None
    })
