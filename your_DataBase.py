import urllib.request
import urllib.parse
import json
from helpers import load_json_data_from_url
from helpers import make_tmdb_api_request
from helpers import movie_info
from helpers import get_api_key
if __name__ == '__main__':
    user_api_key = get_api_key()
    print('Enter path for movie list:')
    filename = input()
    myfile = open(filename, mode='w', encoding='utf-8')
    films = movie_info()
    json.dump(films, myfile)
    myfile.close()

