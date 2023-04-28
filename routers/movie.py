from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieSerives
from schemas.movie import Movie

movie_router= APIRouter()


@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    db =Session()
    result = MovieSerives(db).get_movies()
    return JSONResponse(status_code=200 , content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer)])
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db =Session()
    result = MovieSerives(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrada la pelicula'})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['Movies'], response_model=Movie)
def get_movies_by_category(category: str = Query(max_length=15, min_length=5)) -> Movie:
    db =Session()
    result = MovieSerives(db).get_movie_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrada la pelicula'})
    else:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies/', tags=['Movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    db =Session()
    MovieSerives(db).create_movie(movie)
    return JSONResponse(status_code=200,content={"message": "Se ha registrado la pelicula"}) 

@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    db =Session()
    result = MovieSerives(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrada la pelicula'})
    
    MovieSerives(db).update_movie(id,movie, result)
    return JSONResponse(status_code=200,content={"message": "Se ha modificado la pelicula"}) 

@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    db =Session()
    result = db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrada la pelicula'})
    
    MovieSerives(db).delete_movie(result)
    return JSONResponse(content={"message": "Se ha elimindado la pelicula"}) 