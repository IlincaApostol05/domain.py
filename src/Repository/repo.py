from src.Validators.validate import MovieValidator
from src.domain.domain import Movie
class Movies_Repository:
    def __init__(self):
        self._movies = []
        self._clients=[]


    def add_movie(self,movie_id):
        if movie_id in self._movies:
            raise ValueError('Movie with this id already in list')
            self._movies[movie._movie_id] = movie_id

    def remove_movie(self,id):
        if id in self._movies:
            self._movies.remove(id)
        else:
            raise ValueError('Movie not found')

    def get_all_movies(self):
        return [self._movies[movie_id] for movie_id in self._movies]

    def add_client(self,client):
        if client in self._clients:
            raise ValueError('Client with this id already in the list')
            self._clients[client._client_id] == client


