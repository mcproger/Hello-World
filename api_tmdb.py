import unittest
from tmdb_api_helpers import load_json_data_from_url
from tmdb_api_helpers import make_tmdb_api_request
from tmdb_api_helpers import enter_api_key


def get_saw_film_budget(api_key):
    return make_tmdb_api_request(method='/movie/215', api_key=api_key, extra_params=None)['budget']


if __name__ == '__main__':
    api_key = enter_api_key()
 	print(get_saw_film_budget(api_key))
