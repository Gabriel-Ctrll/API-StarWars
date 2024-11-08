from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.services.starwars_service import get_filmes, get_people, get_naves
from app.models.film import FilmeDetail

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API de Star Wars!"}

@app.get("/filmes", response_model=List[FilmeDetail])
async def filmes(episodio_id: int = Query(None, description="ID do episódio"),
                 titulo: str = Query(None, description="Título do filme")):
    return await get_filmes(episodio_id, titulo)

@app.get("/people")
async def people(nome: str = Query(None, description="Nome do personagem"),
                 genero: str = Query(None, description="Gênero do personagem"),
                 cor_dos_olhos: str = Query(None, description="Cor dos olhos do personagem")):
    return await get_people(nome, genero, cor_dos_olhos)

@app.get("/naves")
async def naves(nome: str = Query(None, description="Nome da nave"),
                fabricante: str = Query(None, description="Fabricante da nave"),
                classe: str = Query(None, description="Classe da nave")):
    return await get_naves(nome, fabricante, classe)