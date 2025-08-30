import spacy

nlp = spacy.load("pt_core_news_sm")

def preprocess_text(text: str) -> str:
    doc = nlp(text)
    tokens = []

    for token in doc:
        if not token.is_stop and not token.is_punct:
            tokens.append(token.lemma_.lower())

    return " ".join(tokens)