from helpers import load_json_data_from_url
from helpers import make_tmdb_api_request
from helpers import movie_budget
from helpers import get_user_api_key
if __name__ == '__main__':
    user_api_key = get_user_api_key()
    print(movie_budget(user_api_key))
