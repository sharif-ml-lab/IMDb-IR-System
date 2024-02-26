from typing import Dict, List

bigram_index = None
movies_dataset = None


def correct_text(
    text: str, bigram_index: Dict[str, List[str]], similar_words_limit: int = 20
) -> str:
    """
    Correct the give query text, if it is misspelled using Jacard similarity

    Paramters
    ---------
    text: str
        The query text

    Returns
    str
        The corrected form of the given text
    """
    return text


def search(
    title_query: str,
    abstract_query: str,
    max_result_count: int,
    method: str = "ltn-lnn",
    weight: float = 0.5,
    should_print=False,
    preferred_field: str = None,
):
    """
    Finds relevant documents to query

    Parameters
    ---------------------------------------------------------------------------------------------------
    max_result_count: Return top 'max_result_count' docs which have the highest scores.
                      notice that if max_result_count = -1, then you have to return all docs

    mode: 'detailed' for searching in title and text separately.
          'overall' for all words, and weighted by where the word appears on.

    where: when mode ='detailed', when we want search query
            in title or text not both of them at the same time.

    method: 'ltn-lnn' or 'ltc-lnc' or 'okapi25'

    preferred_field: A list containing preference rates for each field. If None, the preference rates are equal.

    Returns
    ----------------------------------------------------------------------------------------------------
    list
    Retrieved documents with snippet
    """
    return ["1243523", "6753495", "2342348"]


def get_movie_by_id(id: str, movies_dataset: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Get movie by its id

    Parameters
    ---------------------------------------------------------------------------------------------------
    id: str
        The id of the movie

    movies_dataset: List[Dict[str, str]]
        The dataset of movies

    Returns
    ----------------------------------------------------------------------------------------------------
    dict
        The movie with the given id
    """

    return {
        "Title": "This is movie's title",
        "Summary": "This is a summary",
        "URL": "https://www.imdb.com/title/tt0111161/",
        "Cast": ["Morgan Freeman", "Tim Robbins"],
        "Genres": ["Drama", "Crime"],
        "Image_URL": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg",
    }
