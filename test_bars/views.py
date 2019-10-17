from http.client import HTTPResponse

from django.shortcuts import render


def get_main_page(request):
    return render(request, 'app/main_page.html')
    # return HTTPResponse(False)
    # return render(request, app.main)


def error_page(request):
    return render(request, 'error.html')
