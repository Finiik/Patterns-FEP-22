# main.py
from fastapi import FastAPI
from app.views import app

app_instance = FastAPI()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
