from fastapi import FastAPI
import uvicorn
from app.routers.author import router as author_view_router
from app.routers.book import router as book_view_router

app = FastAPI()
app.include_router(author_view_router)
app.include_router(book_view_router)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
