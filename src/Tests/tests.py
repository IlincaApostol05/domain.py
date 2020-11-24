from src.Validators.validate import ClientValidator,MovieValidator,Rental_validator
from src.domain.domain import clientException,movieException,rentalException,Client,Movie,Rental
from datetime import date
import unittest
from src.services.service import Service,Statistics


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

class Test_Functions(unittest.TestCase):

    def setUp(self):
        self._Test = Service()
        self._Test.add_movie(368,'Avatar','Best movie','Action')
        self._Test.add_movie(647, 'Ted', '2000movie', 'Horror')
        self._Test.add_client(378,'John Snow')
        self._Test.add_client(849,'Mary Donald')
        self._Test.rent_a_movie(566,578,date(2020,11,11),date(2019,11,11))
        self._Test.rent_a_movie(948, 378, date(2020, 11, 11), date(2019, 11, 11))


    def test_movie_list(self):
        self.assertEqual(len(self._Test.get_all_movie,2))


    def test_client_list(self):
        self.assertEqual(len(self._Test.get_all_clients()))


    def test_update_movie(self):
        id=123
        newtitle='Harry Potter 8'
        newdescription='new movie'
        newgenre='action'
        self._Test.update_movies(id,newtitle,newdescription,newgenre)
        for movie in self._Test.get_all_movie():
            self.assertEqual(movie.title,'Harry Potter 8')
            self.assertEqual(movie.description, 'new movie')
            self.assertEqual(movie.genre, 'action')
            break


    def test_update_client(self):
        id=233
        newname='Jack Dan'
        self._Test.update_client(id,newname)
        for client in self._Test.get_all_clients():
            self.assertEqual(client.client_id,233)
            self.assertEqual(client.name,'Jack Dan')
            break


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self._Test =Statistics
        self._Test.max_delay()
        self._Test.id_in_rentals(378)
        self._Test.max_rentals()
        self._Test.most_rented_movies()
        self._Test.sort_late_rentals()
        self._Test.sort_most_active_clients()

    def test_how_days_delay(self):
        id=368
        self._Test.how_days_delay(id)

    def test_how_many_times_rented(self):
        id=378
        self._Test.how_many_times_rented(id)














