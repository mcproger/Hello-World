import json
from helpers import recomend_movies
from helpers import load_movie_list
if __name__ == '__main__':
    movie_list = load_movie_list()
    print('Enter film title: ', end=' ')
    print(recomend_movies(movie_list))



