# import polyglot.text
import spacy

TAGS = (
    'PUNCT', 'SYM', 'ADJ', 'DET', 'ADV', 'ADP', 'VERB', 'CCONJ', 
    'NOUN', 'PROPN', 'PART', 'INTJ', 'PRON', 'SCONJ', 'AUX', 'CONJ'
)

class Extractor():
    def __init__(self, lang='en'):
        self.lang = lang
        self.nlp = spacy.load(lang)

    def extract(self, data):
        if isinstance(data, list):
            return self._extract_multi(data)
        return self._extract_one(data)

    def _extract_one(self, document):
        spacy_doc = self.nlp(document)
        features = {}

        features['length'] = len(document)
        features['tokens'] = len(spacy_doc)
        features['sentences'] = len(list(spacy_doc.sents))
        features['words_per_sents'] = features['tokens'] / features['sentences']
        features['avg_word_size'] = sum(len(word) for word in spacy_doc) / features['tokens']
        features['lex_diversity'] = len(set([word.tag_ for word in spacy_doc])) / features['tokens']
        features['ttr'] = len(set([word for word in spacy_doc])) / features['tokens']

        for tag in TAGS:
            features[f'frequency_{tag}'] = len([1 for token in spacy_doc if token.pos_ == tag]) / features['tokens']

        return features

    def _extract_multi(self, documents):
        return [self._extract_one(document) for document in documents]