from src.domain.domain import Movie, movieException
from src.domain.domain import Client
from datetime import date
from src.domain.domain import clientException
from src.domain.domain import rentalException
from src.domain.domain import Rental
from random import randint
from re import search


class Service:
    """
        Class for the functions that implement the required functionalities.
    """
    def __init__(self,movie_repository,client_repository,rental_repository,movie_validator,client_validator,rental_validator):
        self._movie_repository = movie_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository
        self._movie_validator = movie_validator
        self._client_validator = client_validator
        self._rental_validator = rental_validator

        self._movies = self._movie_repository._movies
        self._clients = self._client_repository._clients
        self._rented = self._rental_repository._rented


        """
        Generates the initial lists of movies,clients and rentals
        """

    @property
    def movies(self):
        return self._movies


    @property
    def clients(self):
        return self._clients


    @property
    def rented(self):
        return self._rented

    def __str__(self):
        return str(self._client_id)+ " "+ self._name


    def add_movie(self,id,title,description,genre):
        """
        This function adds a new movie at the end of the initial list of movies
        :param id: (int)-The id of the movie that we want to add
        :param title: (str)-The title of the movie that we want to add
        :param description: (str)-The description of the movie that we want to add
        :param genre: (str)-The genre of the movie that we want to add
        :return:
        """
        movie = str(Movie(id,title,description,genre))
        for movie in self._movies:
            if id == movie._movie_id:
                raise movieException("Two movies cannot have the same id")
        self._movie_repository.add(movie)




    def remove_movie(self,id):
        """
        This function removes a movie by a given id
        :param id: (int)-The id of the movie we want to remove
        :return:
        """
        found=False
        for movie in self._movies[::-1]:
            if id == movie._movie_id:
                found =True
                self._movie_repository.remove(movie)
        if found == False:
            raise movieException("This movie cannot be removed because it is not in the list")


    def update_movies(self,id,new_title,new_description,new_genre):
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
                movie._title = new_title
                movie._description = new_description
                movie._genre = new_genre
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
        for client in self._clients:
            if id == client._client_id:
                raise clientException("Two clients cannot have the same id")
        self._client_repository.add(client)


    def remove_client(self,id):
        """
        This function removes a client from the list list of clients by a given id
        :param id: (int)-The id of the client
        :return: -
        """
        found=False
        for client in self._clients[::-1]:
            if id == client._client_id:
                found = True
                self._client_repository.remove(client)
        if found == False:
            raise clientException("This client cannot be removed because it is not in the list")


    def update_client(self,id,new_name):
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
                client._name = new_name
        return found


    def have_rented(self,client_id):
        """
        This function search if a client has rented movies that passed their due date for return
        :param client_id: The id(int) of the client
        :return: False if we find such a client,true otherwise
        """
        found=0
        for client in self._rented[::-1]:
            if client_id == client._client_id:
                if client._returned_date > client.due_date:
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
            for movie in self._movies:
                if self.have_rented(client_id) == 0:
                    if movie_id == movie._movie_id:
                        found1 = 1
                        rented = Rental(randint(10000,90000),movie_id,client_id,rented_day,given_day,'0')
                        self._rented.append(rented)
        if self.have_rented(client_id) == 1:
            raise rentalException("This client cannot rent a movie")
        if found1 == 0:
            raise rentalException("This movie is not available,it is not in the list")


    def return_a_movie(self, client_id, movie_id, returned_days):
        """
        This function return a movie at a given day
        :param client_id: The id(int) of the client who wants to return the movie
        :param movie_id: The id(int) of the movie that should be returned
        :param returned_days: The moment when the client wants to return the movie
        :return:
        """
        found = 0
        for rent in self._rented:
            if rent._returned_date == '0':
                if client_id == rent._client_id:
                    if movie_id == rent._movie_id:
                        found = 1
                        rent._returned_date = returned_days

        if found == 0:
            raise ValueError("But this movie was returned!")


    def find_movie_by_title(self,semi_title):
        """
        This function find a movie by a given partial title
        :param semititle:The partial title given
        :return:The list with the movies we are searching for
        """
        list = []
        for index in range(len(self._movies)):
            if search(semi_title , self._movies[index]._title):
                list.append(str(self._movies[index]._movie_id)+" "+self._movies[index]._title+" "+self._movies[index]._description+""+self._movies[index]._genre)
        return list


    def find_client_by_name(self,seminame):
        """
        This function find a client by a given partial name
        :param seminame: The partial name given
        :return: The list with the clients we are searching for
        """
        list =[]
        for index in range(len(self._clients)):
            if search(seminame,self._clients[index]._name):
                list.append(str(self._clients[index]._client_id)+" "+self._clients[index]._name)
        return list

    def get_all_movie(self):
        return self._movie_repository.get_all_movies()


    def get_all_rentals(self):
        return self._rental_repository.get_all_rentals()


    def get_all_clients(self):
        return self._client_repository.get_all_clients()


class Statistics:
    def __init__(self,service):
        self._service =service
        self._movies=self._service._movies
        self._clients = self._service._clients
        self._rented = self._service._rented


    def how_many_times_rented(self,this_movie):
        """
        This function calculates how many times a movie was rented
        :param thismovie: The movie(int) given by the user
        :return: The nr(int) = how many times a movie was rented
        """
        nr=0
        for index in self._rented[::-1]:
            if index._movie_id == this_movie:
                nr=nr+1
        return nr


    def max(self):
        """
        This function calculates the maximum sum = how many times appeared the movie that was rented most often
        :return: The max(int)
        """
        max=0
        for index in self._rented:
            if self.how_many_times_rented(index._movie_id) > max:
                max = self.how_many_times_rented(index._movie_id)
        return max


    def id_in_rentals(self,id):
        """
        This function check if a given movie was rented
        :param id: The id of the movie given by the user
        :return:
        """
        found=False
        for index in self._movies:
            for index2 in self._rented:
                if index._movie_id == index2._movie_id==id:
                    found=True
        return found


    def most_rented_movies(self):
        """
        This function provide the list of movies, sorted in descending order of the number of days they were rented.
        :return:The list
        """
        new_list=[]
        max=self.max()
        for j in range(max+1,-1,-1):
            for index in self._movies[:]:
                if self.how_many_times_rented(index._movie_id) == j:
                    new_list.append(str(index._movie_id)+" "+index._title+" "+index._genre+" "+index._description)
        return new_list


    def has_past(self,movie_id):
        """
        This function tell us if a rented movie passed it due date for return
        :param movieid: The movie id(int) given by the user
        :return: True if had passed,False otherwise
        """
        passed = False
        for index in self._rented:
            if index._movie_id == movie_id:
                if index._returned_date > index._due_date:
                    passed=True
        return passed


    def how_days_delay(self,movie_id):
        """
        This function computes the number of days that passed for a rented movie=returned_date-due_date
        :param movieid: The movie id given by the user
        :return: The number of days
        """
        number_of_days=0
        for index in self._rented:
            if index._movie_id == movie_id:
                if self.has_past(movie_id) == True:
                    number_of_days = number_of_days + abs((index._returned_date - index._due_date).days)
        return number_of_days


    def max_delay(self):
        """
        This function find the rented movie with the biggest delay and returns it
        :return: max(int)-the rented movie with the biggest delay
        """
        max = 0
        for index in self._rented[::-1]:
            if self.how_days_delay(index._movie_id) > max:
                max = max + self.how_days_delay(index._movie_id)
        return max


    def sort_late_rentals(self):
        """
        This function sort in descending order->
        ->All the movies that are currently rented, for which the due date for return has passed and put them in a new list
        :return:The new list
        """
        new_list=[]
        max=self.max_delay()
        for index in range(max+1,0,-1):
            for j in self._movies:
                if self.how_days_delay(j._movie_id) == index:
                    new_list.append(str(j._movie_id) + " " + j._title + " " + j._genre + " " + j._description)
        return new_list


    def sum_rentals(self,client):
        """
        This function computes the total rentals for a client,which is equal with the sum
         of the (returned_date-rented_date) for every rented movie
        :param client: The id(int) of a client given by the user in order to calculate the sum
        :return:
        """
        sum = 0
        for index in self._rented:
            if client == index._client_id:
                sum+=abs((index._returned_date - index._rented_date).days)
        return sum


    def max_rentals(self):
        """
        This function search for the client with the biggest sum of rentals and return that sum
        :return: The max(int)=the biggest sum of rentals
        """
        max=0
        for index in self._clients:
            if self.sum_rentals(index._client_id) >max:
                max =max+ self.sum_rentals(index._client_id)
        return max


    def sort_most_active_clients(self):
        """
        This function provides the new list of movies sorting in descending order of the number of movie rental days they have
        :return:The new list
        """
        new_list=[]
        max=self.max_rentals()
        for index in range(max + 1, -1, -1):
            for j in self._clients:
                if self.sum_rentals(j._client_id) == index:
                    new_list.append(str(j._client_id) + " " + j._name)
        return new_list

    def __len__(self):
        return len(self._clients)


class Test_Service:
    """
    Class to test the functions
    """
    def __init__(self):
        pass

    def test_add_movie(self):
        service = Service()
        try:
            service.add_movie(123,'Alladin','Children movie','Animation')
        except movieException:
            assert True


    def test_add_client(self):
        service = Service()
        try:
            service.add_client(123,'Brown Nathan')
        except clientException:
            assert True


    def test_remove_movie(self):
        service = Service()
        try:
            service.remove_movie(948)
        except movieException:
            assert True


    def test_remove_client(self):
        service = Service()
        try:
            service.remove_movie(758)
        except clientException:
            assert True

    def test_update_movies(self):
        id=123
        try:
            Service.update_movies(id)
        except movieException:
            assert True

    def test_update_clients(self):
        id=123
        try:
            Service.update_client(id)
        except clientException:
            assert True

    def test_rent_movie(self):
        client_id=1233
        movie_id=123
        rented_day=date(2020,11,11)
        given_date=date(2020,12,12)
        try:
            Service.rent_a_movie(client_id,movie_id,rented_day,given_date)
        except movieException:
            assert True

    def test_return_movie(self):
        client_id=123
        movie_id=489
        return_date=date(2019,11,11)
        try:
            Service.return_a_movie(client_id,movie_id,return_date)
        except movieException:
            assert True

    def test_all(self):
        Test_Service.test_add_movie(self)
        Test_Service.test_add_client(self)
        Test_Service.test_remove_movie(self)
        Test_Service.test_remove_client(self)
        Test_Service.test_update_movies(self)
        Test_Service.test_update_clients(self)

#Test_Service.test_all(True)




























            


