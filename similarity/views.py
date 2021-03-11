from django.shortcuts import render
from django.views.generic import View

from similarity.forms import TextForm


class TextView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {'form': TextForm()}
        return render(request=request,
                      template_name=self.template_name,
                      context=context)

    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            scores = form.evaluate()
            context['scores'] = scores

        return render(request=request,
                      template_name=self.template_name,
                      context=context)
