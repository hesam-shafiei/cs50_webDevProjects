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


def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entryInfo = util.get_entry(entry_search)
        isEmpty = entryInfo == None
        html_content = None
        if(not isEmpty):
            html_content = markdowner.convert(entryInfo)
        else:
            html_content = None

        if html_content is not None:
            return render(request, "encyclopedia/entryPage.html", {
                "title": entry_search,
                "entryInfo": html_content,
                "isEmpty": isEmpty
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = markdowner.convert(content)
            return render(request, "encyclopedia/entryPage.html", {
                title: title,
                "content": html_content
            })