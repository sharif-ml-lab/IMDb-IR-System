import json
from typing import List


def check_field_types(json_file_path, expected_fields):
    with open(json_file_path, "r") as file:
        data = json.load(file)


    # check len of the data
    assert len(data) > 1000, f"Expected at least 1000 movies, but got {len(data)}"

    # check data types
    for movie in data:
        for field, expected_type in expected_fields.items():
            if field not in movie or movie[field] is None:
                print(f'Expected field {field} not found in movie {movie["id"]}')
            else:    
                if expected_type is not None:
                    if expected_type == str:    
                        assert isinstance(
                            movie[field], expected_type
                        ), f'Expected field {field} to be of type {expected_type}, but got {type(movie[field])} in movie {movie["id"]}'
                    if expected_type == List[str]:
                        assert isinstance(
                            movie[field], list
                        ), f'Expected field {field} to be of type {expected_type}, but got {type(movie[field])} in movie {movie["id"]}'
                        assert all(
                            isinstance(x, str) for x in movie[field]
                        ), f'Expected field {field} to be of type {expected_type}, but got {type(movie[field])} in movie {movie["id"]}'


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

json_file_path = "../IMDB_crawled.json"
check_field_types(json_file_path, expected_fields)
