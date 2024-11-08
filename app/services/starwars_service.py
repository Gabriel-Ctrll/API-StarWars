import httpx
from fastapi import HTTPException
from app.utils.api_utils import fetch_data
from app.models.film import FilmeDetail

async def get_filmes(episodio_id: int = None, titulo: str = None):
    url = "https://swapi.dev/api/films/"
    async with httpx.AsyncClient() as client:
        filmes = await fetch_data(url, client)
        
        if episodio_id:
            filmes = [filme for filme in filmes if filme["episode_id"] == episodio_id]
        if titulo:
            filmes = [filme for filme in filmes if titulo.lower() in filme["title"].lower()]

        filmes_detalhados = []
        for filme in filmes:
            detalhes = FilmeDetail(
                title=filme["title"],
                episode_id=filme["episode_id"],
                opening_crawl=filme["opening_crawl"],
                director=filme["director"],
                producer=filme["producer"],
                release_date=filme["release_date"],
                characters=filme["characters"],
                planets=filme["planets"],
                starships=filme["starships"],
                vehicles=filme["vehicles"],
                species=filme["species"]
            )
            filmes_detalhados.append(detalhes)

        return filmes_detalhados

async def get_people(nome: str = None, genero: str = None, cor_dos_olhos: str = None):
    url = "https://swapi.dev/api/people/"
    async with httpx.AsyncClient() as client:
        people = await fetch_data(url, client)

        if nome:
            people = [person for person in people if nome.lower() in person["name"].lower()]
        if genero:
            people = [person for person in people if genero.lower() == person["gender"].lower()]
        if cor_dos_olhos:
            people = [person for person in people if cor_dos_olhos.lower() in person["eye_color"].lower()]

        personagens_detalhados = []
        for person in people:
            detalhes = {
                "name": person["name"],
                "height": person["height"],
                "mass": person["mass"],
                "hair_color": person["hair_color"],
                "skin_color": person["skin_color"],
                "eye_color": person["eye_color"],
                "birth_year": person["birth_year"],
                "gender": person["gender"],
                "films": person["films"],
                "species": person["species"],
                "vehicles": person["vehicles"],
                "starships": person["starships"],
                "homeworld_name": person["homeworld"]
            }
            personagens_detalhados.append(detalhes)

        return personagens_detalhados

async def get_naves(nome: str = None, fabricante: str = None, classe: str = None):
    url = "https://swapi.dev/api/starships/"
    async with httpx.AsyncClient() as client:
        naves = await fetch_data(url, client)

        if nome:
            naves = [nave for nave in naves if nome.lower() in nave["name"].lower()]
        if fabricante:
            naves = [nave for nave in naves if fabricante.lower() in nave["manufacturer"].lower()]
        if classe:
            naves = [nave for nave in naves if classe.lower() in nave["starship_class"].lower()]

        naves_detalhadas = []
        for nave in naves:
            detalhes = {
                "name": nave["name"],
                "model": nave["model"],
                "manufacturer": nave["manufacturer"],
                "cost_in_credits": nave["cost_in_credits"],
                "length": nave["length"],
                "max_atmosphering_speed": nave["max_atmosphering_speed"],
                "crew": nave["crew"],
                "passengers": nave["passengers"],
                "cargo_capacity": nave["cargo_capacity"],
                "consumables": nave["consumables"],
                "hyperdrive_rating": nave["hyperdrive_rating"],
                "starship_class": nave["starship_class"]
            }
            naves_detalhadas.append(detalhes)

        return naves_detalhadas