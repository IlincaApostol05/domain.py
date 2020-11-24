from src.ui.console import Console
from src.domain.domain import Movie
from src.domain.domain import Client,Rental
from src.services.service import Service,Statistics
from src.Validators.validate import MovieValidator,ClientValidator,Rental_validator
from src.Repository.repo import Rental_Repository,Movies_Repository,Client_Repository
from datetime import date

client=Client(client_id=39,name='Will Thomas')
movie= Movie(movie_id=9123,title="Toy Story 3,",description="A true story",genre="Action")
rental=Rental(rental_id=367,movie_id=833,client_id=483,rented_date=date(2020,11,11),due_date=date(2020,11,11),returned_date=date(2020,11,11))
movie_repository=Movies_Repository()
client_repository=Client_Repository()
rental_repository=Rental_Repository(movie_repository,client_repository)
movie_validator=MovieValidator(movie)
client_validator=ClientValidator(client)
rental_validator =Rental_validator(rental)
service = Service(movie_repository,client_repository,rental_repository,movie_validator,client_validator,rental_validator)
statistics = Statistics(service)
console = Console(service,statistics)
console.start_command_ui()