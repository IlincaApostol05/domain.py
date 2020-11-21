from src.domain.domain import clientException,movieException,rentalException
from src.Validators.validate import ClientValidator,MovieValidator
"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
class Console:

    def __init__(self, service):
        self._service = service



    def show_menu_ui(self):
        print("1.Display movies")
        print("2.Display clients")
        print("3.Display rentals")
        print("4.Add movie")
        print("5.Remove movie")
        print("6.Update movies")
        print("7.Add client")
        print("8.Remove client")
        print("9.Update clients")
        print("10.Rent movie")
        print("11.Return movie")
        print("12.Exit")

    def display_movies_ui(self):
        for movie in self._service._movies:
            print(str(str(movie.movie_id) + " " + str(movie._title) + " " + movie._description + " " + movie._genre))


    def display_clients_ui(self):
        for client in self._service._clients:
            print(str(str(client._client_id)+" "+str(client._name)))


    def display_rentals_ui(self):
        for rental in self._service._rented:
            print(str(str(rental._rental_id)+" "+str(rental._movie_id)+" "+str(rental._client_id)+" "+str(rental._rented_date)+" "+str(rental._due_date)+" "+str(rental._returned_date)))


    def add_movie_ui(self):
        id = int(input("id:"))
        title = str(input("title:"))
        description = str(input("description:"))
        genre = str(input("genre:"))
        self._service.add_movie(id,title,description,genre)


    def remove_movie_ui(self):
        id = int(input("Which movie you want to remove?Give me the id:"))
        self._service.remove_movie(id)


    def update_movies_ui(self):
        id = int(input("Which id you want to update?:"))
        title = str(input("New title:"))
        description = str(input("New descriptiion:"))
        genre = str(input("New genre:"))
        self._service.update_movies(id,title,description,genre)


    def add_client_ui(self):
        id=int(input("id:"))
        name=str(input("name:"))
        self._service.add_client(id,name)


    def remove_client_ui(self):
        id=int(input("Which client you want to remove?Give me the id:"))
        self._service.remove_client(id)


    def update_client_ui(self):
        id = int(input("Which client you want to update?Give me the id:"))
        name= str(input("New name:"))
        self._service.update_client(id,name)


    def rent_movie_ui(self):
        client_id = int(input("Who wants to rent a movie?Give me the id:"))
        movie_id= int(input("What movie?Give me the id:"))
        rented_day=input("When this client wants to rent?:")
        given_day=input("Until when this movie cand be rented?:")
        self._service.rent_a_movie(client_id,movie_id,rented_day,given_day)


    def return_movie_ui(self):
        client_id=int(input("Who wants to return a movie?Give me the id:"))
        movie_id = int(input("What movie?Give me the id:"))
        returned_days=input("When this client wants to return the movie?:")
        self._service.return_a_movie(client_id,movie_id,returned_days)


    def start_command_ui(self):
        done = False
        self.show_menu_ui()
        while not done:
            try:
                command = input("Your choice is:")
                if command == '1':
                    self.display_movies_ui()
                elif command == '2':
                    self.display_clients_ui()
                elif command == '3':
                    self.display_rentals_ui()
                elif command == '4':
                    self.add_movie_ui()
                elif command == '5':
                    self.remove_movie_ui()
                elif command == '6':
                    self.update_movies_ui()
                elif command == '7':
                    self.add_client_ui()
                elif command == '8':
                    self.remove_client_ui()
                elif command == '9':
                    self.update_client_ui()
                elif command == '10':
                    self.rent_movie_ui()
                elif command == '11':
                    self.return_movie_ui()
                elif command == '12':
                    done =True
                    print("Bye bye!")
                else:
                    print("Bad input")
            except movieException as me:
                print(str(me))
            except clientException as ce:
                print(str(ce))
            except rentalException as re:
                print(str(re))
            except ValueError as ve:
                print(str(ve))





