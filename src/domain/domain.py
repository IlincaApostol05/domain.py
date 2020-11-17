from datetime import date
class movieException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

class Movie:
    """
        Represent one movie
    """
    def __init__(self,movie_id, title, description, genre):
        '''
        Create movies with:
        :param movie_id: Each movie has an id(integer,unique)
        :param title: Each movie has a title(string)
        :param description: Each movie has a description(string)
        :param genre: Each movie has a genre(string)
        '''
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre

    @movie_id.setter
    def movie_id(self, value):
        self._movie_id = value

    @title.setter
    def title(self, other1):
        self._title = other1

    @description.setter
    def description(self, other1):
        self._description = other1

    @genre.setter
    def genre(self, other1):
        self._genre = other1

    def __str__(self):
        return str(self._movie_id) +" "+self._title+" "+self._description+" "+self._genre


class clientException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class Client:
    """
    Represent one client
    """
    def __init__(self,client_id,name):
        '''
        Create clients with:
        :param client_id: Each client has an id(integer,unique)
        :param name: Each client has a name(string)
        '''
        self._client_id = client_id
        self._name = name

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return str(self._client_id)+ " "+ self._name


class rentalException(Exception):
    def __init__(self, msg):
        self._msg = msg


    def __str__(self):
        return self._msg


class Rental:
    '''
    Represent one rental
    '''
    def __init__(self,rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        '''
        Create rentals with:
        :param rental_id: Each rental has an id(integer,unique)
        :param movie_id: Each movie has an id(integer,unique)
        :param client_id: Each client has an id(integer,unique)
        :param rented_date: Each client has a rented_date(date)
        :param due_date:Each client has a due_date(date)
        :param returned_date:Each client has a returned_date(date)
        '''
        self._rental_id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    def __str__(self):
        return 'rented id:'+str(self._rental_id) + " "+'movie id:' + str(self._movie_id)+" "+'client id:'+str(self._client_id)+" "+'rented date:'+str(self._rented_date)+" "+'due date:'+str(self._due_date)+" "+'returned date:'+str(self._returned_date)


    @property
    def rental_id(self):
        return self._rental_id

    @property
    def due_date(self):
        return self._due_date

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def returned_date(self):
        return self._returned_date


def test_Movie():
    movie = Movie(1234,'adventure time','best movie','action')
    assert 1234 == movie._movie_id
    assert 'adventure time' == movie._title
    assert 'best movie' == movie._description
    assert 'action' == movie._genre


def test_Client():
    client = Client(123,'John White')
    assert 123 == client._client_id
    assert 'John White' == client._name


def test_Rental():
    rental = Rental(123,456,789,date(2015,9,12),date(2015,7,12),date(2015,8,12))
    assert 123 == rental._rental_id
    assert 456 == rental._movie_id
    assert 789 == rental._client_id
    assert date(2015,9,12) == rental._rented_date
    assert date(2015,7,12) == rental._due_date
    assert date(2015,8,12) == rental._returned_date


def test_domain():
    test_Movie()
    test_Client()
    test_Rental()

#test_domain()