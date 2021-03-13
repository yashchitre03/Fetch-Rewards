from django.shortcuts import render
from django.views.generic import View

from similarity.forms import TextForm


class TextView(View):
    """
    Renders the HTML view depending on the type of request (GET, POST).
    """

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        """
        Fetches empty form and renders the HTML.
        :param request: Request object
        :param args: None
        :param kwargs: None
        :return: Response object
        """
        context = {'form': TextForm()}

        return render(request=request,
                      template_name=self.template_name,
                      context=context)

    def post(self, request, *args, **kwargs):
        """
        Processes the form data and returns the updated HTML.
        :param request: Request object
        :param args: None
        :param kwargs: None
        :return: Response object
        """
        form = TextForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            scores = form.evaluate()
            context['scores'] = scores

        return render(request=request,
                      template_name=self.template_name,
                      context=context)
