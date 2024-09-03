from fastapi import FastAPI
from fastapi.responses import HTTPResponse

app = FastAPI()
app.title = 'My First FastAPI App'
app.version = '0.0.1'

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse(content='<h1>Welcome to FastAPI</h1>', status_code=200)


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies