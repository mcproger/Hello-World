from helpers import load_movie_list
from helpers import get_movie_by_key_word
if __name__ == '__main__':
    movie_list = load_movie_list()
    print('Enter key word:', end=' ')
    print(get_movie_by_key_word(movie_list))