from src.domain.domain import Movie, movieException
from src.domain.domain import Client
from datetime import date
from src.domain.domain import clientException
from src.domain.domain import rentalException
from src.domain.domain import Rental
from random import randint
from src.Validators.validate import ClientValidator,MovieValidator,Rental_validator


class Service:
    """
        Class for the functions that implement the required functionalities.
    """
    def __init__(self):
        """
        Generates the initial lists of movies,clients and rentals
        """
        self._movies = [Movie(1726, "| Alice in wonderland |","The best animated movie |", "Animation"),
                        Movie(8374, "| Da Vinci Code |", "What are the secrets of Paris? |", "Mistery"),
                        Movie(4739, "| No time to die |", "2020 movie |", "Action", ),
                        Movie(2314, "| Annabell |", "See if you can resist |", "Horror"),
                        Movie(1849, "| The Secret |", "The secret to leading a successful life |", "Documentary"),
                        Movie(1348, "| Mister Bean |", "Try not to laugh |", "Comedy"),
                        Movie(1949, "| Inferno |", "It is true what Dante said? |", "Thriller"),
                        Movie(8634, "| The invisible guest |", "Who will solve the crime..? |", "Police"),
                        Movie(9237, "| Jurassic World |", "What would life be with dinosaurs? |", "SF"),
                        Movie(3847, "| Word War two |", "What really happened in Word War two?","History")]

        self._clients = [Client(164, "Olivia Smith"),
                        Client(273, "Sophia Robinson"),
                        Client(934, "Charlie Anderson"),
                        Client(830, "Harry Wright"),
                        Client(293, "Charlotte Brown"),
                        Client(334, "Thomas Edwards"),
                        Client(732, "Ruby White"),
                        Client(139, "Henry Moore"),
                        Client(456, "Ben Jones"),
                        Client(528, "Dylan Martin")]
        self._rented = []
        for index in range(len(self._movies)-1):
            for index2 in self._clients:
                self._rented.append(Rental(randint(10000,90000),self._movies[index]._movie_id,index2._client_id,date(randint(2015,2017),randint(1,10),randint(1,30)),date(randint(2018,2020),randint(11,12),randint(1,30)),date(randint(2018,2020),randint(1,12),randint(1,30))))
                index+=1
            break



    @property
    def clients(self):
        return self._clients

    @property
    def rented(self):
        return self._rented



    def add_movie(self,id,title,description,genre):
        """
        This function adds a new movie at the end of the initial list of movies
        :param id: (int)-The id of the movie that we want to add
        :param title: (str)-The title of the movie that we want to add
        :param description: (str)-The description of the movie that we want to add
        :param genre: (str)-The genre of the movie that we want to add
        :return:
        """
        movie = Movie(id,title,description,genre)
        for index in self._movies[::-1]:
            if id == index._movie_id:
               raise movieException("Two movies cannot have the same id")
        self._movies.append(movie)
        print("Movie succesfully added")


    def remove_movie(self,id):
        """
        This function removes a movie by a given id
        :param id: (int)-The id of the movie we want to remove
        :return:
        """
        found=False
        for index in self._movies[::-1]:
            if id == index._movie_id:
                found =True
                self._movies.remove(index)
                print("Movie succesfully removed")
        if found == False:
            raise movieException("This movie cannot be removed because it is not in the list")


    def update_movies(self,id,newtitle,newdescription,newgenre):
        """
        This function update the list of movies.It will change the title,description and genre of a movie by a given id
        :param id: (int)-The id of the movie we want to update.This will be not changed
        :param newtitle: (str)-The update title of the movie
        :param newdescription: (str)-The update description of the movie
        :param newgenre: (str)-The update genre of the movie
        :return: True if the updates were made,false otherwise
        """
        found = False
        for movie in self._movies:
            if id == movie._movie_id:
                found =True
                movie._title = newtitle
                movie._description = newdescription
                movie._genre = newgenre
                print("Movie successfully updated")
        if found == False:
            raise movieException("This movie cannot be updated because it is not in the list")



    def add_client(self,id,name):
        """
        This function adds a client at the end of the initial list of clients
        :param id: (int)-The id of the client
        :param name: (str)-The name of the client
        :return:
        """
        client=Client(id,name)
        for index in self._clients:
            if id == index._client_id:
                raise clientException("Two clients cannot have the same id")
        self._clients.append(client)
        print("Client succesfully added")


    def remove_client(self,id):
        """
        This function removes a client from the list list of clients by a given id
        :param id: (int)-The id of the client
        :return: -
        """
        found=False
        for index in self._clients[::-1]:
            if id == index._client_id:
                found = True
                self._clients.remove(index)
                print("Client succesfully removed")
        if found == False:
            raise clientException("This client cannot be removed because it is not in the list")


    def update_client(self,id,newname):
        """
        This function updates the list of clients.It will change the name of the client with a given id
        :param id:
        :param newname:
        :return:
        """
        found = False
        for client in self._clients:
            if id == client._client_id:
                found = True
                client._name = newname
                print("Client successfully updated")
        return found


    def have_rented(self,client_id):
        """
        This function search if a client has rented movies that passed their due date for return
        :param client_id: The id(int) of the client
        :return: False if we find such a client,true otherwise
        """
        found=0
        for index in self._rented[::-1]:
            if client_id == index._client_id:
                if index._returned_date > index.due_date:
                    found=1
        return found


    def rent_a_movie(self,client_id,movie_id,rented_day,given_day):
        """
        This function adds a new rent at the end of the initial list of rentals
        :param client_id: The id(int) of the client who wants to rent a movie
        :param movie_id: The id(int) of the movie he/she wants to rent
        :param rented_day: The day(date) when he/she wants to rent the movie
        :param given_day: The day(date) until he can rent that movie
        :return: -
        """
        found1 = 0
        if rented_day > given_day:
            found1=2
            raise rentalException("Rented day must be bigger than due date")
        elif rented_day <= given_day:
            for index in self._movies:
                if self.have_rented(client_id) == 0:
                    if movie_id == index._movie_id:
                        found1 = 1
                        rented = Rental(randint(10000,90000),movie_id,client_id,rented_day,given_day,"0")
                        self._rented.append(rented)
                        print("Movie succesfully rented")
        if self.have_rented(client_id) == 1:
            raise rentalException("This client cannot rent a movie")
        if found1 == 0:
            raise rentalException("This movie is not available,it is not in the list")



    def return_a_movie(self,client_id,movie_id,returned_days):
        """
        This function return a movie at a given day
        :param client_id: The id(int) of the client who wants to return the movie
        :param movie_id: The id(int) of the movie that should be returned
        :param returned_days: The moment when the client wants to return the movie
        :return:
        """
        found=0
        for index in self._rented:
            if index._returned_date == '0':
                if client_id == index._client_id:
                    if movie_id == index._movie_id:
                        found = 1
                        index._returned_date = returned_days
                        print("Movie succesfully returned")
                        break
        if found == 0:
            raise movieException("But this movie was returned!")



