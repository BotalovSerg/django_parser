from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Choice


def index(request):
    return render(request, 'index.html')


def index_page(request):
    res = Choice.objects.all()
    context = {
        'all_user': res
    }
    return render(request, 'app/index_page.html', context)


def page_message(request, pag):
    # res = Choice.objects.get(pk=pag)
    res = get_object_or_404(Choice, pk=pag)
    context = {
        'user': res
    }
    return render(request, 'app/page_user.html', context=context)
