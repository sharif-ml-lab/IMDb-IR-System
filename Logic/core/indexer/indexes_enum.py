from enum import Enum


class Indexes(Enum):
    DOCUMENTS = 'documents'
    STARS = 'stars'
    GENRES = 'genres'
    SUMMARIES = 'summaries'

class Index_types(Enum):
    TIERED = 'tiered'
    DOCUMENT_LENGTH = 'document_length'
    METADATA = 'metadata'