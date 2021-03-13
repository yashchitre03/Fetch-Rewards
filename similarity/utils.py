class ReadOnly:
    """
    Marks the class attributes as read-only (i.e. client cannot update the values).
    """

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        raise AttributeError('read-only attribute')


class SimilarityCalculator:
    """
    Contains different algorithms to calculate the similarity between two text samples
    """

    punctuations = set(r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
    text1, text2 = ReadOnly(), ReadOnly()
    v1, v2 = ReadOnly(), ReadOnly()

    def __init__(self, text1, text2):
        self._text1, self._text2 = text1, text2
        self._v1, self._v2 = self.to_vector()

    def to_vector(self) -> (list[int], list[int]):
        """
        Converts the text samples to vector representations.
        :return: list vectors for both the samples
        """
        data1, data2 = self.clean_samples()
        vocab = tuple(set(data1 + data2))

        v1 = list(map(lambda word: data1.count(word), vocab))
        v2 = list(map(lambda word: data2.count(word), vocab))

        return v1, v2

    def clean_samples(self) -> (list[str], list[str]):
        """
        Calls clean method for both the text samples.
        :return: list of words for both the samples
        """
        def clean(value: str) -> list[str]:
            """
            Removes punctuations and non-alphabet words from the sample.
            :param value: text sample
            :return: list of cleaned words
            """
            text = value.lower()
            clean_text = ''.join(filter(lambda c: c not in self.punctuations, text))
            words = clean_text.split()
            filtered_words = list(filter(lambda word: word.isalpha(), words))
            return filtered_words

        return clean(self.text1), clean(self.text2)

    def execute(self, method: str) -> float:
        """
        Runs the desired algorithm on the samples.
        :param method: the algorithm name that needs to be executed
        :return: similarity score between the samples rounded to 4 decimals
        """
        try:
            score = getattr(self, f'_{method}')()
        except ZeroDivisionError:
            score = 0

        return round(score, 4)

    def _jaccard(self) -> float:
        """
        https://en.wikipedia.org/wiki/Jaccard_index
        :return: Jaccard Index similarity score
        """
        intersect, total = 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            total += e1 + e2

        return intersect / (total - intersect)

    def _cosine(self) -> float:
        """
        https://en.wikipedia.org/wiki/Cosine_similarity
        :return: Cosine similarity score
        """
        def dot(x: list[int], y: list[int]) -> int:
            """
            Calculates the dot product of two vectors.
            :param x: first vector
            :param y: second vector
            :return: dot product
            """
            res = 0
            for e1, e2 in zip(x, y):
                res += e1 * e2

            return res

        return dot(self.v1, self.v2) / (dot(self.v1, self.v1) * dot(self.v2, self.v2)) ** 0.5

    def _dice(self) -> float:
        """
        https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
        :return: Dice's Coefficient similarity score
        """
        intersect, total = 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            total += e1 + e2

        return 2 * intersect / total

    def _overlap(self) -> float:
        """
        https://en.wikipedia.org/wiki/Overlap_coefficient
        :return: Overlap Coeffcient similarity score
        """
        intersect, v1_sum, v2_sum = 0, 0, 0

        for e1, e2 in zip(self.v1, self.v2):
            intersect += min(e1, e2)
            v1_sum += e1
            v2_sum += e2

        return intersect / min(v1_sum, v2_sum)
