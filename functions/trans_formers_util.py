from sentence_transformers import SentenceTransformer

class TransFormersEmbedding:

    def __init__(self, embeder):
        self.embeder = SentenceTransformer(embeder)

    def embedding_text(self, text):
        try:
            return self.embeder.encode(text, convert_to_numpy=True, normalize_embeddings=True), None
        except Exception as err:
            return None, err
