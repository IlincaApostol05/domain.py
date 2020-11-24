from src.ui.console import Console
from src.domain.domain import Movie
from src.domain.domain import Client
from src.services.service import Service,Statistics

client=Client(client_id=39,name='Will Thomas')
movie= Movie(movie_id=9123,title="Toy Story 3,",description="A true story",genre="Action")
service = Service()
statistics = Statistics(service)
console = Console(service,statistics)
console.start_command_ui()