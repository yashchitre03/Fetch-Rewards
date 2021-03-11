class SimilarityCalculator:

    def __init__(self, t1, t2):
        self.t1 = t1.lower()
        self.t2 = t2.lower()

    def jaccard(self):
        t1_unique = set(self.t1.split())
        t2_unique = set(self.t2.split())
        t1_intersect_t2 = len(t1_unique & t2_unique)
        t1_union_t2 = len(t1_unique | t2_unique)

        try:
            score = round(t1_intersect_t2 / t1_union_t2, 4)
        except ZeroDivisionError:
            score = 0

        return score

    def cosine(self):
        # TODO: implement
        return 1
