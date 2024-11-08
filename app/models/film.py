from pydantic import BaseModel
from typing import List

class FilmeDetail(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: List[str] = []
    planets: List[str] = []
    starships: List[str] = []
    vehicles: List[str] = []
    species: List[str] = []
    
    class Config:
        orm_mode = True