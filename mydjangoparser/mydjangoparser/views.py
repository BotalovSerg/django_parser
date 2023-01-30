from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View

from app.forms import GetForms


class HomePageView(View):
    form_class = GetForms
    initial = {'key': 'value'}
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            qu = form.cleaned_data['locations'] + "+" + form.cleaned_data['keyword']
            return HttpResponseRedirect('/app/')

        return render(request, self.template_name, {'form': form})
