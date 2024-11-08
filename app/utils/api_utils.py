import httpx
from fastapi import HTTPException

async def fetch_data(url: str, client: httpx.AsyncClient):
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()["results"]
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar {url}: {str(e)}")