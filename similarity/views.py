from django.shortcuts import render
from django.views.generic import FormView

from similarity.forms import TextForm


class TextView(FormView):
    template_name = 'home.html'
    form_class = TextForm

    def form_valid(self, form):
        score = form.evaluate()
        context = self.get_context_data()
        context['score'] = score

        return render(request=self.request,
                      template_name='home.html',
                      context=context)
