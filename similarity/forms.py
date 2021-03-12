from django import forms

from .utils import SimilarityCalculator


class TextForm(forms.Form):
    algo_choices = {'jaccard': 'Jaccard Index',
                    'cosine': 'Cosine Similarity',
                    'dice': 'Dice\'s Coefficient',
                    'overlap': 'Overlap Coefficient'}

    t1 = forms.CharField(label='Text 1', widget=forms.Textarea)
    t2 = forms.CharField(label='Text 2', widget=forms.Textarea)
    algo = forms.MultipleChoiceField(help_text='Shift-click to or Ctrl-click to select multiple items',
                                     label='Algorithm', choices=algo_choices.items())

    def evaluate(self):
        first = self.cleaned_data['t1']
        second = self.cleaned_data['t2']
        choices = self.cleaned_data['algo']

        calc = SimilarityCalculator(first, second)
        scores = []
        for choice in choices:
            score = calc.execute(choice)
            scores.append((self.algo_choices.get(choice), score))

        return scores
