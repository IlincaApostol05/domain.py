from src.Validators.validate import ClientValidator,MovieValidator,Rental_validator
from src.domain.domain import clientException,movieException,rentalException,Client,Movie,Rental
from datetime import date
import unittest


class Test_ClientValidator:
    def __init__(self):
        pass

    @staticmethod
    def test_validate_client_name():
        c1 = Client(123, 'Ariana')
        c2 = Client(234, '')
        c3 = Client(657, 'Anthony White')
        clients = [c1, c2, c3]

        for i in range(0, len(clients)):
            try:
                ClientValidator.validate_client_name(ClientValidator(clients[i]))
            except clientException as ce:
                print(ce)
                print(clients)
                print()


    @staticmethod
    def test_validate_client_id():
        c1 = Client(827, 'Sam')
        c2 = Client(346, '')
        c3 = Client('', 'Sean Anthony')
        c4 = Client(346,'Sam Winchester')
        clients = [c1, c2, c3,c4]

        for i in range(0, len(clients)):
            try:
                ClientValidator.validate_client_id(ClientValidator(clients[i]))
            except clientException as ce:
                print(ce)
                print(clients)
                print()

    @staticmethod
    def run_all_tests_clients():
        Test_ClientValidator.test_validate_client_name()
        Test_ClientValidator.test_validate_client_id()


#Test_ClientValidator.run_all_tests_clients()


class Test_Movie_Validator:
    def __init__(self):
        pass

    @staticmethod
    def test_validate_movie_id():
        c1 = Movie(' ', 'The apocalypse','Apocalyptic movie','Action')
        c2 = Movie(234, 'Black House','House','Comedy')
        c3 = Movie(657, 'Scary Movie','Laugh and cry','Horror')
        movies = [c1, c2, c3]

        for i in range(0, len(movies)):
            try:
                MovieValidator.validate_movie_id(MovieValidator(movies[i]))
            except movieException as me:
                print(me)
                print(movies)
                print()


    @staticmethod
    def test_validate_movie_title():
        c1 = Movie(457, 'Harry Potter', 'The most famous movie', 'Action')
        c2 = Movie(824, ' ', 'Who is the killer', 'Crime')
        c3 = Movie(928, 'Mr Bean', 'Try not to laugh', 'Comedy')
        movies = [c1, c2, c3]

        for i in range(0, len(movies)):
            try:
                MovieValidator.validate_movie_title(MovieValidator(movies[i]))
            except movieException as me:
                print(me)
                print(movies)
                print()


    @staticmethod
    def test_validate_movie_description():
        c1 = Movie(387, 'Harry Potter', ' ', 'Action')
        c2 = Movie(839, 'The killer', ' Who killed the girl ', 'Crime')
        c3 = Movie(239, 'Mr Bean', 'Try not to laugh', 'Comedy')
        movies = [c1, c2, c3]

        for i in range(0, len(movies)):
            try:
                MovieValidator.validate_movie_description(MovieValidator(movies[i]))
            except movieException as me:
                print(me)
                print(movies)
                print()


    @staticmethod
    def test_validate_movie_genre():
        c1 = Movie(982, 'Harry Potter', 'The most famous movie', ' ')
        c2 = Movie(475, 'The killer', 'Who is the killer', 'Crime Movie')
        c3 = Movie(258, 'Mr Bean', 'Try not to laugh', 'Comedy')
        movies = [c1, c2, c3]

        for i in range(0, len(movies)):
            try:
                MovieValidator.validate_movie_genre(MovieValidator(movies[i]))
            except movieException as me:
                print(me)
                print(movies)
                print()

    @staticmethod
    def run_all_tests_movies():
        Test_Movie_Validator.test_validate_movie_id()
        Test_Movie_Validator.test_validate_movie_title()
        Test_Movie_Validator.test_validate_movie_description()
        Test_Movie_Validator.test_validate_movie_genre()

#Test_Movie_Validator.run_all_tests_movies()

class Test_Rentals_Validation:
    def __init__(self):
        pass

    @staticmethod
    def test_validate_rental_id():
        c1 = Rental('',2467,2345,date(2020,12,12),date(2020,12,12),date(2020,12,12))
        c2 = Rental(234,2643,2345,date(2020,12,12),date(2020,12,12),date(2020,12,12))
        c3 = Rental(657,4876,2735,date(2020,12,12),date(2020,12,12),date(2020,12,12))
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_rental_id(Rental_validator(rentals[i]))
            except rentalException as re:
                print(re)
                print(rentals)
                print()

    @staticmethod
    def test_validate_movie_id():
        c1 = Rental(748, 2467, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c2 = Rental(234, '', 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c3 = Rental(657, 4876, 2735, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_movie_id(Rental_validator(rentals[i]))
            except rentalException as re:
                print(re)
                print(rentals)
                print()


    @staticmethod
    def test_validate_client_id():
        c1 = Rental(895, 2467, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c2 = Rental(234, 2643, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c3 = Rental(657, 4876, '', date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_client_id(Rental_validator(rentals[i]))
            except clientException as re:
                print(re)
                print(rentals)
                print()


    @staticmethod
    def test_validate_due_date():
        c1 = Rental(123, 2467, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c2 = Rental(234, 2643, 2345, date(2020, 12, 12), '', date(2020, 12, 12))
        c3 = Rental(657, 4876, 2735, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_due_date(Rental_validator(rentals[i]))
            except rentalException as re:
                print(re)
                print(rentals)
                print()


    @staticmethod
    def test_validate_rented_date():
        c1 = Rental(123, 2467, 2345, '', date(2020, 12, 12), date(2020, 12, 12))
        c2 = Rental(234, 2643, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c3 = Rental(657, 4876, 2735, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_rented_date(Rental_validator(rentals[i]))
            except rentalException as re:
                print(re)
                print(rentals)
                print()


    @staticmethod
    def test_validate_returned_date():
        c1 = Rental(123, 2467, 2345, date(2020, 12, 12), date(2020, 12, 12), date(2020, 12, 12))
        c2 = Rental(234, 2643, 2345, date(2020, 12, 12), date(2020, 10, 12), date(2020, 12, 12))
        c3 = Rental(657, 4876, 2735, date(2020, 12, 12), date(2020, 12, 12), '')
        rentals = [c1, c2, c3]

        for i in range(0, len(rentals)):
            try:
                Rental_validator.validate_returned_date(Rental_validator(rentals[i]))
            except rentalException as re:
                print(re)
                print(rentals)
                print()

    @staticmethod
    def run_all_tests_rentals():
        Test_Rentals_Validation.test_validate_movie_id()
        Test_Rentals_Validation.test_validate_rental_id()
        Test_Rentals_Validation.test_validate_client_id()
        Test_Rentals_Validation.test_validate_due_date()
        Test_Rentals_Validation.test_validate_rented_date()
        Test_Rentals_Validation.test_validate_returned_date()

#Test_Rentals_Validation.run_all_tests_rentals()


class MovieTest(unittest.TestCase):
    def test_movie(self):
        movie = Movie(467,'Avatar','2000','Action')
        self.assertEqual(movie.movie_id,467)
        self.assertEqual(movie.title, 'Avatar')
        self.assertEqual(movie.description, '2020')
        self.assertEqual(movie.genre, 'Action')


class ClientTest(unittest.TestCase):
    def test_client(self):
        client = Client(123,'Robert White')
        self.assertEqual(client.client_id,123)
        self.assertEqual(client.name)


class RentalTest(unittest.TestCase):
    def test_rental(self):
        rental = Rental(123,456,789,date(2002,11,11),date(2019,10,10),date(2020,11,12))
        self.assertEqual(rental.rental_id,123)
        self.assertEqual(rental.movie_id,456)
        self.assertEqual(rental.client_id,789)
        self.assertEqual(rental.rented_date,date(2002,11,11))
        self.assertEqual(rental.due_date,date(2019,10,10))
        self.assertEqual(rental.returned_date,date(2020,11,12))


#MovieTest.test_movie(True)
#ClientTest.test_client(True)
#RentalTest.test_rental(True)










