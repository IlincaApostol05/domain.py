from datetime import datetime,date,time,timedelta,timezone
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
        print("<display movies>")
        print("<display clients>")
        print("<display rentals>")
        print("<add movie>")
        print("<add client>")
        print("<remove movie>")
        print("<remove client>")
        print("<update movies>")
        print("<update clients>")
        print("<rent movie>")
        print("<return movie>")
        print("<exit>")


    def split_command(self, command):
        """
        Divide user command into command word and command parameters
        :param command: user command
        :return: command word, parameters
        """
        command_as_words = command.strip().split(' ', 1)
        command_as_words[0] = command_as_words[0].strip().lower()
        return command_as_words[0], '' if len(command_as_words) == 1 else command_as_words[1].strip()


    def diplay_list_ui(self,command_parameters):
        parameters = command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movies":
            for movie in self._service.movies:
                print(movie)
        elif len(parameters) == 1 and parameters[0] == "clients":
            for client in self._service.clients:
                print(client)
        elif len(parameters) == 1 and parameters[0] == "rentals":
            for index in range(len(self._service.rented)):
                print(self._service.rented[index])
        else:
            print("Try again")


    def add_command_ui(self,command_parameters):
        parameters = command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movie":
            id=int(input("id:"))
            title=str(input("title:"))
            description=str(input("description:"))
            genre=str(input("genre:"))
            self._service.add_movie(id,title,description,genre)
        elif len(parameters) == 1 and parameters[0] == "client":
            id = int(input("id:"))
            name = str(input("name:"))
            self._service.add_client(id,name)
        else:
            print("Try again")


    def update_command_ui(self,command_parameters):
        parameters= command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movies":
            id=int(input("enter an existing id:"))
            newtitle = str(input("new title:"))
            newdescription = str(input("new description:"))
            newgenre = str(input("new genre:"))
            self._service.update_movies(id,newtitle,newdescription,newgenre)
            print("Movies succesfully updated")
        elif len(parameters) == 1 and parameters[0] == "clients":
            id = int(input("enter an existing id:"))
            newname = str(input("new name:"))
            self._service.update_client(id,newname)
            print("Clients succesfully updated")
        else:
            print("Try again")



    def remove_command_ui(self,command_parameters):
        parameters = command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movie":
            id = int(input("id:"))
            self._service.remove_movie(id)
        elif len(parameters) == 1 and parameters[0] == "client":
            id = int(input("id:"))
            self._service.remove_client(id)
        else:
            print("Try again")


    def rent_a_movie_ui(self,command_parameters):
        parameters = command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movie":
            client = int(input("Who wants to rent a movie?Give me his/her id:"))
            movie = int(input("Which movie he/she wants to rent?Give me the id?:"))
            rented_day = input("When he/she wants to rent it?:")
            day = input(("Until this movie can be rented?:"))
            self._service.rent_a_movie(client,movie,rented_day,day)
        else:
            print('Try again')



    def return_a_movie_ui(self,command_parameters):
        parameters = command_parameters.split()
        if len(parameters) == 1 and parameters[0] == "movie":
            client = int(input("Who wants to return a movie?Give me his/her id:"))
            movie = int(input("Which movie he/she wants to return?Give me the id?:"))
            return_day =str(input("When he/she wants to return it?:"))
            self._service.return_a_movie(client,movie,return_day)
        else:
            print("Try again")



    def start_command_ui(self):
        self.show_menu_ui()
        movies=[]
        self._service.test_init_movies(movies)
        clients=[]
        self._service.test_init_clients(clients)
        rented=[]
        self._service.test_init_rented(rented)
        command_dictionary={"add":self.add_command_ui, "remove":self.remove_command_ui,"display":self.diplay_list_ui,'update':self.update_command_ui,
                            "rent":self.rent_a_movie_ui,'return':self.return_a_movie_ui}
        done = False
        while not done:
            command = input("Your choice is:")
            command_word, command_parameters = self.split_command(command)
            if command_word in command_dictionary:
                try:
                    command_dictionary[command_word](command_parameters)
                except ValueError as ve:
                    print(str(ve))
            elif 'exit' == command_word:
                print("Bye bye")
                done = True
            else:
                print("Bad command!")
