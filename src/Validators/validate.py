from src.domain.domain import movieException
from src.domain.domain import clientException,rentalException


class ClientValidator:

    def __init__(self, client):
        self.clients = client


    def validate_client_name(self):
        "check empty"
        if self.clients._name == '':
            raise clientException("The entered name is invalid!")
        command_parameters = self.clients._name.split(' ')
        "check if the name is composed by firstname and lastname"
        if len(command_parameters) != 2:
            raise clientException("The name should be composed of one firstname and one lastname!")
        if not command_parameters[0].isalpha():
            raise clientException("The entered name is invalid!")
        if not command_parameters[1].isalpha():
            raise clientException("The entered name is invalid!")


    def validate_client_id(self):
        "check empty"
        if self.clients.client_id == '':
            raise clientException("The entered id is invalid!")


class MovieValidator:

    def __init__(self,movie):
        self.movies = movie


    def validate_movie_id(self):
        "check empty"
        if self.movies._movie_id == '':
            raise movieException("The entered id is invalid!")


    def validate_movie_title(self):
        "check empty"
        if self.movies._title == '':
            raise movieException("The entered title is invalid!")


    def validate_movie_description(self):
        "check empty"
        if self.movies._description == '':
            raise movieException("The entered description is invalid!")


    def validate_movie_genre(self):
        "check empty"
        if self.movies._genre == '':
            raise movieException("The entered genre is invalid!")
        command_parameters = self.movies._genre.split(' ')
        "check if genre is bigger than one word"
        if len(command_parameters) != 1:
            raise movieException("The genre should be composed of one word!")
        if not command_parameters[0].isalpha():
            raise movieException("The entered genre is invalid!")


class Rental_validator:
    def __init__(self, rental):
        self.rentals = rental


    def validate_rental_id(self):
        "check empty"
        if self.rentals._rental_id == '':
            raise rentalException("The entered id is invalid!")


    def validate_movie_id(self):
        "check empty"
        if self.rentals._movie_id == '':
            raise rentalException("The entered id is invalid!")


    def validate_client_id(self):
        "check empty"
        if self.rentals._rental_id == '':
            raise rentalException("The entered id is invalid!")



    def validate_rented_date(self):
        "check empty"
        if self.rentals._rented_date == '':
            raise rentalException("The entered rented date is invalid!")


    def validate_due_date(self):
        "check empty"
        if self.rentals._due_date == '':
            raise rentalException("The entered due date is invalid!")


    def validate_returned_date(self):
        "check empty"
        if self.rentals._returned_date == '':
            raise rentalException("The entered returned date is invalid!")
        "check if due date is bigger than returned date"
        if self.rentals._returned_date > self.rentals._due_date:
            raise rentalException("Due date must be bigger than returned date")











