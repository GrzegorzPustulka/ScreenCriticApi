from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from screen_critic.crud.category import category as crud_category
from screen_critic.crud.movie import movie as crud_movie
from screen_critic.schemas.movie import MovieRead

from ...schemas.category import CategoryRead
from ..deps import get_db

router = APIRouter(prefix="/movie", tags=["movie"])


@router.get("/search", status_code=status.HTTP_200_OK, response_model=list[MovieRead])
def search_movies(db: Session = Depends(get_db)):
    movies = crud_movie.get_all(db)
    list_movies = []
    for movie in movies:
        name = crud_category.get(db, movie.category_id).name
        list_movies.append(MovieRead(**jsonable_encoder(movie), category_name=name))

    return list_movies


@router.get(
    "/name/{movie_name}", response_model=list[MovieRead], status_code=status.HTTP_200_OK
)
def read_movies_by_name(movie_name: str, db: Session = Depends(get_db)):
    movies = crud_movie.get_by_name(db, movie_name)
    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    list_movies = []
    for movie in movies:
        name = crud_category.get(db, movie.category_id).name
        list_movies.append(MovieRead(**jsonable_encoder(movie), category_name=name))
    return list_movies


@router.get("id/{movie_id}", response_model=MovieRead, status_code=status.HTTP_200_OK)
def read_movie_by_id(movie_id: str, db: Session = Depends(get_db)):
    movie = crud_movie.get(db, movie_id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    name = crud_category.get(db, movie.category_id).name
    return MovieRead(**jsonable_encoder(movie), category_name=name)


@router.get(
    "/categories", response_model=list[CategoryRead], status_code=status.HTTP_200_OK
)
def read_categories(db: Session = Depends(get_db)):
    categories = crud_category.get_all(db)
    return CategoryRead(**jsonable_encoder(categories))


@router.get(
    "/random/{category_id}", response_model=MovieRead, status_code=status.HTTP_200_OK
)
def random_movie(category_id: str, db: Session = Depends(get_db)):
    movie = crud_movie.get_random(category_id, db)
    name = crud_category.get(db, movie.category_id).name
    return MovieRead(**jsonable_encoder(movie), category_name=name)
