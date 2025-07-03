from fastapi import FastAPI
import _asyncio
from src.services.scrapper import scrape_landing_page
from pydantic import BaseModel

class ScrapeRequest(BaseModel):
    url: str

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.post("/scrape")
async def scrapper(request: ScrapeRequest):
    await scrape_landing_page(url=request.url)
    return {"status": "scraped", "url": request.url}
