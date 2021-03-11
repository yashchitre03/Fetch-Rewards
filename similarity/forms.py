from django import forms


class TextForm(forms.Form):
    t1 = forms.CharField(label='Text 1', widget=forms.Textarea)
    t2 = forms.CharField(label='Text 2', widget=forms.Textarea)

    def evaluate(self):
        first = self.cleaned_data['t1'].lower()
        second = self.cleaned_data['t2'].lower()

        first_unique = set(first.split())
        second_unique = set(second.split())
        first_intersect_second = len(first_unique & second_unique)
        first_union_second = len(first_unique | second_unique)

        try:
            similarity = round(first_intersect_second / first_union_second, 4)
        except ZeroDivisionError:
            similarity = 0

        return similarity
