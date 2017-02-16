import urllib.request
import urllib.parse
import json

#======================================Ввод Api-ключа пользователя======================================================
from getpass import getpass
def get_api_key():
    print('Enter your api key v3')
    user_api_key = getpass('Enter your api key v3')
    return user_api_key
#=======================================================================================================================
def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)
def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

#===============================1задача=================================================================================
def movie_budget(user_api_key):
    return make_tmdb_api_request(method='/movie/215', api_key=user_api_key, extra_params=None)['budget']

#===============================2задача=================================================================================
def movie_info():
    films = []
    films_quantity = 0
    number_of_film = 1
    while films_quantity < 1000:
        try:
            films.append(make_tmdb_api_request(method='/movie/%d' % number_of_film, api_key=user_api_key, extra_params=None))
        except:
            number_of_film = number_of_film + 1
        else:
            number_of_film = number_of_film + 1
            films_quantity = films_quantity + 1
    return films


#===============================3задача=================================================================================

def load_movie_list():
    print('Enter path to your movie list:')
    filename = input()
    myfile = open(filename, mode='r', encoding='utf-8')
    movie_list = json.load(myfile)
    return movie_list

def get_movie_by_key_word(movie_list):
    key_word = input().capitalize()
    for film in movie_list:
        if film['original_title'].find(key_word) != -1:
            print(film['original_title'])
    return ' '


#===============================4задача=================================================================================
def recomend_movies(movie_list):
    films = []
    key_word = input()
    for film in movie_list:
        if film['original_title'] == key_word:
            films.append(film['original_title'])
            films.append(film['budget'])
            films.append(film['vote_average'])

    for film in movie_list:
        if ((film['original_title'] == films[0]) or (int(film['budget']) == int(films[1])) or (film['vote_average'] == films[2])):
            print(film['original_title'])

    return ' '

