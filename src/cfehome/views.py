from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def home_page_view(request: HttpRequest) -> HttpResponse:
    my_title = "My Home Page"
    my_context = {
        "title": my_title,
        "my_text": "This is about me",
    }
    html_template  = "home.html"
    
    return render(request, html_template, my_context)
    
    