from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from visits.models import PageVisit



def home_view(request: HttpRequest) -> HttpResponse:
    return about_view(request)
    
    
def about_view(request: HttpRequest) -> HttpResponse:
    PageVisit.objects.create(path=request.path)
    
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path).order_by('-timestamp')
    
    try:
        percent = (page_qs.count() / qs.count()) * 100
    except ZeroDivisionError:
        percent = 0

    my_title = "About Page"
    my_context = {
        "title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    html_template  = "about.html"

    return render(request, html_template, my_context)