from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from .models import Choice
from .forms import GetForms

from .logic import ParserMain


# class IndexView(FormView):
#     form_class = GetForms
#     template_name = 'index.html'
#     model = Choice
#     success_url = '/'
#
#     # parser = ParserMain()
#
#     def form_valid(self, form):
#         qu = form.cleaned_data['locations'] + "+" + form.cleaned_data['keyword']
#         # self.parser.get_data(qu)
#         return super().form_valid(form)


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
