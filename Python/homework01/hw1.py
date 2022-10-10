class CountVectorizer:
    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def get_tokens(self, document: str) -> list:
        if self.lowercase:
            document = document.lower()
        tokens = document.split()
        return tokens

    def fit(self, corpus: list):
        """Learn the vocabulary"""
        i = 0
        for document in corpus:
            tokens = self.get_tokens(document)
            for token in tokens:
                if token not in self._vocabulary:
                    self._vocabulary[token] = i
                    i += 1

        return self

    def transform(self, corpus: list) -> list:
        """Calculate the document-term matrix"""
        count_matrix = []
        for document in corpus:
            row = [0] * len(self._vocabulary)
            tokens = self.get_tokens(document)
            for token in tokens:
                row[self._vocabulary[token]] += 1
            count_matrix.append(row)
        return count_matrix

    def fit_transform(self, corpus: list) -> list:
        return self.fit(corpus).transform(corpus)

    def get_feature_names(self) -> list:
        return list(self._vocabulary.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names()

    correct_ans_1 = ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                     'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    correct_ans_2 = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    print(features)
    print(count_matrix)

    if features == correct_ans_1:
        print('Test 1: OK')
    else:
        print('Test 1: Failed')

    if count_matrix == correct_ans_2:
        print('Test 2: OK')
    else:
        print('Test 2: Failed')
