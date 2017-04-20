import unittest
import api_tmdb
from tmdb_api_helpers import load_json_data_from_url
from tmdb_api_helpers import make_tmdb_api_request
from tmdb_api_helpers import enter_api_key


#print(api_tmdb.get_saw_film_budget('1ebe2aa78b39fafdbbf3f9e6833a99e5'))
class FirstTest(unittest.TestCase):
	def test_first(self):
		res = api_tmdb.get_saw_film_budget('1ebe2aa78b39fafdbbf3f9e6833a99e5')
		self.assertEqual(res, 4000000)

if __name__ == "__main__":
	unittest.main()
