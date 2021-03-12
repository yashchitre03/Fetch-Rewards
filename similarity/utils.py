class Preprocessor:
    punctuations = set(r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        text = value.lower()
        clean_text = ''.join(filter(lambda c: c not in self.punctuations, text))
        words = clean_text.split()
        filtered_words = list(filter(lambda word: word.isalpha(), words))

        setattr(instance, self.private_name, filtered_words)


class SimilarityCalculator:
    t1 = Preprocessor()
    t2 = Preprocessor()

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def jaccard(self):
        print(self.t1, self.t2)
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
        vocab = tuple(set(self.t1 + self.t2))
        t1_unique = set(self.t1)
        t2_unique = set(self.t2)

        v1 = list(map(lambda word: 1 if word in t1_unique else 0, vocab))
        v2 = list(map(lambda word: 1 if word in t2_unique else 0, vocab))

        try:
            score = self.dot(v1, v2) / (self.dot(v1, v1) * self.dot(v2, v2))**0.5
        except ZeroDivisionError:
            score = 0

        return round(score, 4)

    @staticmethod
    def dot(x, y):
        res = 0
        for x_elem, y_elem in zip(x, y):
            res += x_elem * y_elem

        return res
