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

    @staticmethod
    def dot(x, y):
        res = 0
        for x_elem, y_elem in zip(x, y):
            res += x_elem * y_elem

        return res

    def manhattan(self):
        pass

    def euclidean(self):
        pass

    def jaccard(self):
        t1_unique = set(self.t1)
        t2_unique = set(self.t2)
        t1_intersect_t2 = len(t1_unique & t2_unique)
        t1_union_t2 = len(t1_unique | t2_unique)

        try:
            score = t1_intersect_t2 / t1_union_t2
        except ZeroDivisionError:
            score = 0

        return round(score, 4)

    def cosine(self):
        v1, v2 = self.to_vector()

        try:
            score = self.dot(v1, v2) / (self.dot(v1, v1) * self.dot(v2, v2)) ** 0.5
        except ZeroDivisionError:
            score = 0

        return round(score, 4)

    def dice(self):
        pass

    def matching(self):
        pass

    def overlap(self):
        pass
