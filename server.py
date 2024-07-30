from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s %(message)s")

@app.get("/")
def read_root():
    logging.info("Root endpoint was called")
    return {"Hello": "World"}

@app.get("/page/{page_id}")
def read_item(page_id: int, q: str = None):
    logging.info(f"Item endpoint was called with page_id: {page_id} and query: {q}")
    return {"page_id": page_id, "q": q}
