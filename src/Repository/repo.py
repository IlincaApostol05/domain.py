from src.domain.domain import Movie,Client,Rental
from datetime import date
from random import randint
import secrets


class RepositoryException(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


class Movies_Repository:
    """
    Class used for Movies Repository
    """
    def __init__(self):
        self._movies = [Movie(1726, "| Alice in wonderland |","The best animated movie |", "Animation"),
                        Movie(1989, "| Da Vinci Code |", "What are the secrets of Paris? |", "Mistery"),
                        Movie(1237, "| No time to die |", "2020 movie |", "Action", ),
                        Movie(2314, "| Annabell |", "See if you can resist |", "Horror"),
                        Movie(8499, "| The Secret |", "The secret to leading a successful life |", "Documentary"),
                        Movie(1647, "| Mister Bean |", "Try not to laugh |", "Comedy"),
                        Movie(1849, "| Inferno |", "It is true what Dante said? |", "Thriller"),
                        Movie(4739, "| The invisible guest |", "Who will solve the crime..? |", "Police"),
                        Movie(9237, "| Jurassic World |", "What would life be with dinosaurs? |", "SF"),
                        Movie(1856, "| Word War two |", "What really happened in Word War two?","History")]


    def __len__(self):
        return len(self._movies)

    def __str__(self):
        return str()

    @property
    def movies(self):
        return self._movies


    def add(self, movie):
        """
            Adds a new movie to the repo
            :param movie: A movie stored in a list
            :return: -
        """
        if movie in self._movies:
            raise RepositoryException('Movie already exists!')
        self._movies.append(movie)


    def remove(self, movie):
        """
            Removes the movie with given id
            :param movie_id: The ID of the movie
            :return: -
        """
        return self._movies.remove(movie)

    def get_all_movies(self):
        """
            Gets all the movies
            :return: A list containing all the movies
        """
        return self._movies



class Client_Repository:
    """
    Class used for Client Repository
    """
    def __init__(self):
        self._clients = [Client(164, "Olivia Smith"),
                         Client(273, "Sophia Jones"),
                         Client(934, "Charlie Anderson"),
                         Client(830, "Harry Wright"),
                         Client(293, "Charlotte Brown"),
                         Client(334, "Thomas Edwards"),
                         Client(732, "Ruby White"),
                         Client(139, "Henry Moore"),
                         Client(456, "Ben Jones"),
                         Client(528, "Dylan Martin")]

    def __len__(self):
        return len(self._clients)

    def add(self, client):
        """
            Adds a new client to the repo
            :param movie: A movie stored in a list
            :return: -
        """
        if client in self._clients:
            raise RepositoryException('Client already exists!')
        self._clients.append(client)


    def remove(self, client):
        """
            Removes the client with given id
            :param movie_id: The ID of the client
            :return: -
        """
        return self._clients.remove(client)

    def get_all_clients(self):
        """
            Gets all the clients
            :return: A list containing all the clients
        """
        return self._clients[:]



class Rental_Repository:
    """
    Class used for Rental Repository
    """
    def __init__(self,movie_repository,client_repository):
        self._movies=movie_repository._movies
        self._clients=client_repository._clients

        self._rented = []
        self._movie_id = []
        self._client_id = []
        for index in self._movies:
            self._movie_id.append(index._movie_id)
        for index1 in self._clients:
            self._client_id.append(index1._client_id)
        for index in range(len(self._movies)):
            self._rented.append(Rental(randint(10000, 90000), secrets.choice(self._movie_id), secrets.choice(self._client_id),
                       date(randint(2015, 2017), randint(1, 10), randint(1, 30)),
                       date(randint(2018, 2020), randint(11, 12), randint(1, 30)),
                       date(randint(2018, 2020), randint(1, 12), randint(1, 30))))
            index += 1


    def __len__(self):
        return len(self._rented)

    def add(self, rental):
        """
            Adds a new rental to the repo
            :param movie: A rental stored in a list
            :return: -
        """
        self._rented.append(rental)

    def remove(self, rental_id):
        """
            Removes the rental with given id
            :param movie_id: The ID of the rental
            :return: -
        """
        return self._rented.pop(rental_id)

    def get_all_rentals(self):
        """
            Gets all the rentals
            :return: A list containing all the rentals
        """
        return self._rented[:]



def test_movies_repo():
    movie_repository=Movies_Repository()
    assert len(movie_repository) == 0
    movie1=Movie(1237,'Avatar','Best movie','Action')
    movie_repository.add(movie1)
    assert len(movie_repository) == 1
    movie2=Movie(7484,'Star Wars','2020','Action')
    movie_repository.add(movie2)
    assert len(movie_repository) == 2
    movie3 = Movie(7484, 'Beauty and the beast', 'Kids show', 'Animation')
    try:
        movie_repository.add(movie3)
    except RepositoryException as re:
        assert str(re) == 'Movie already exists!'
    try:
        movie_repository.remove(1237)
    except RepositoryException as re:
        assert str(re) == 'No movie with that id!'


def test_client_repo():
    client_repository=Client_Repository()
    assert len(client_repository) == 0
    client1=Client(738,'John Martin')
    client_repository.add(client1)
    assert len(client_repository) == 1
    client2=Client(289,'Ann Madie')
    client_repository.add(client2)
    assert len(client_repository) == 2
    client3=Client(739,'Richard James')
    try:
        client_repository.add(client3)
    except RepositoryException as re:
        assert str(re) == 'Client already exists!'
    try:
        client_repository.remove(738)
    except RepositoryException as re:
        assert str(re) == 'Client not in the list!'

def test_rental_repo():
    rental_repository=Rental_Repository()
    assert len(rental_repository) == 0
    rental1=Rental(123,839,234,date(2020,11,11),date(2020,12,12),date(2020,12,12))
    rental_repository.add(rental1)
    assert len(rental_repository) == 1
    rental2=Rental(2839,38,489,date(2020,11,11),date(2020,12,12),date(2020,12,12))
    rental_repository.add(rental2)

def test_all():
    test_movies_repo()
    test_client_repo()
    test_rental_repo()

#test_all()





