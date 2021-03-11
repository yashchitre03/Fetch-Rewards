from django import forms

from .utils import SimilarityCalculator


class TextForm(forms.Form):
    algo_choices = {'jaccard': 'Jaccard Similarity (Jaccard index)',
                    'cosine': 'Cosine Similarity', }

    t1 = forms.CharField(label='Text 1', widget=forms.Textarea)
    t2 = forms.CharField(label='Text 2', widget=forms.Textarea)
    algo = forms.MultipleChoiceField(label='Algorithm', choices=algo_choices.items())

    def evaluate(self):
        first = self.cleaned_data['t1']
        second = self.cleaned_data['t2']
        choices = self.cleaned_data['algo']

        calc = SimilarityCalculator(first, second)
        scores = []
        for choice in choices:
            score = getattr(calc, choice)()
            scores.append((self.algo_choices.get(choice), score))

        return scores
