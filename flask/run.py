from app import app
from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn

# initial FastAPI
fastapi_app = FastAPI()

fastapi_app.mount("/flask", WSGIMiddleware(app))

@fastapi_app.get("/fastapi")
def read_main():
    return {"message": "Hi this is fastapi."}

if __name__ == '__main__':
    uvicorn.run(fastapi_app)

