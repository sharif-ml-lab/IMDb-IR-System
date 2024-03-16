import json
from typing import List


def type_check(obj, expected_type):
    if not hasattr(expected_type, "__origin__"):
        return isinstance(obj, expected_type)

    assert expected_type.__origin__ == list, "only list type is supported"
    inner_type = expected_type.__args__[0]
    return isinstance(obj, list) and all(type_check(item, inner_type) for item in obj)


def check_field_types(json_file_path, expected_fields):
    with open(json_file_path, "r") as file:
        data = json.load(file)
    # check len of the data
    assert len(data) >= 1000, f"Expected at least 1000 movies, but got {len(data)}"

    # check data types
    for movie in data:
        for field, expected_type in expected_fields.items():
            if field not in movie or movie[field] is None:
                print(
                    f'Warning: Expected field {field} not found in movie {movie["id"]}'
                )
            else:
                assert type_check(
                    movie[field], expected_type
                ), f'Error: Expected field {field} to be of type {expected_type}, but got {type(movie[field])} in movie {movie["id"]}'


expected_fields = {
    "id": str,
    "title": str,
    "first_page_summary": str,
    "release_year": str,
    "mpaa": str,
    "budget": str,
    "gross_worldwide": str,
    "rating": str,
    "directors": List[str],
    "writers": List[str],
    "stars": List[str],
    "related_links": List[str],
    "genres": List[str],
    "languages": List[str],
    "countries_of_origin": List[str],
    "summaries": List[str],
    "synopsis": List[str],
    "reviews": List[List[str]],
}

json_file_path = "../IMDB_Crawled.json"
check_field_types(json_file_path, expected_fields)
