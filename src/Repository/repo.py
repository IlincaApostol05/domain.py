from src.Validators.validate import MovieValidator

class Movies_Repository:
    def __init__(self):
        self._movies = []


    def add_movie(self,movie):
        if movie._movie_id in self._movies:
            raise ValueError('Movie with this id is already in list')
            self._movies[movie.id] = movie
            
