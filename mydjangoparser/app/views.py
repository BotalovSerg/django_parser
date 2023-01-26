from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice
from .forms import GetForms


class IndexView(generic.ListView):
    form_class = GetForms
    template_name = 'index.html'
    model = Choice

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# def index(request):
#     return render(request, 'index.html')


class ListUsers(generic.ListView):
    template_name = 'app/index_page.html'
    context_object_name = 'all_user'

    def get_queryset(self):
        return Choice.objects.all()


# def index_page(request):
#     res = Choice.objects.all()
#     context = {
#         'all_user': res
#     }
#     return render(request, 'app/index_page.html', context)

class PageMessage(generic.ListView):
    template_name = 'app/page_user.html'
    context_object_name = 'user'

    def get_queryset(self):
        return Choice.objects.get(pk=self.kwargs['pk'])

# def page_message(request, pag):
#     # res = Choice.objects.get(pk=pag)
#     res = get_object_or_404(Choice, pk=pag)
#     context = {
#         'user': res
#     }
#     return render(request, 'app/page_user.html', context=context)
