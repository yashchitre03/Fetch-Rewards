class ReadOnly:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        raise AttributeError('read-only attribute')


class SimilarityCalculator:
    punctuations = set(r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
    text1, text2 = ReadOnly(), ReadOnly()
    v1, v2 = ReadOnly(), ReadOnly()

    def __init__(self, text1, text2):
        self._text1, self._text2 = text1, text2
        self._v1, self._v2 = self.to_vector()

    def to_vector(self):
        data1, data2 = self.clean_samples()
        vocab = tuple(set(data1 + data2))

        v1 = list(map(lambda word: data1.count(word), vocab))
        v2 = list(map(lambda word: data2.count(word), vocab))

        return v1, v2

    def clean_samples(self):
        def clean(value):
            text = value.lower()
            clean_text = ''.join(filter(lambda c: c not in self.punctuations, text))
            words = clean_text.split()
            filtered_words = list(filter(lambda word: word.isalpha(), words))
            return filtered_words

        return clean(self.text1), clean(self.text2)

    def execute(self, method):
        try:
            score = getattr(self, f'_{method}')()
        except ZeroDivisionError:
            score = 0

        return round(score, 4)

    def _jaccard(self):
        intersect, total = 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            total += e1 + e2

        return intersect / (total - intersect)

    def _cosine(self):
        def dot(x, y):
            res = 0
            for x_elem, y_elem in zip(x, y):
                res += x_elem * y_elem

            return res

        return dot(self.v1, self.v2) / (dot(self.v1, self.v1) * dot(self.v2, self.v2)) ** 0.5

    def _dice(self):
        intersect, total = 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            total += e1 + e2

        return 2 * intersect / total

    def _overlap(self):
        intersect, v1_sum, v2_sum = 0, 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            v1_sum += e1
            v2_sum += e2

        return intersect / min(v1_sum, v2_sum)
