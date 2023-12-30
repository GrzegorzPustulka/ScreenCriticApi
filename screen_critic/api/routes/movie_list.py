from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from screen_critic.api.deps import get_current_user, get_db
from screen_critic.crud.category import category as crud_category
from screen_critic.crud.movie import movie as crud_movie
from screen_critic.crud.movie_list import movie_list as crud_movie_list
from screen_critic.models import User
from screen_critic.schemas.movie_list import (
    MovieListCreate,
    MovieListCreateInDb,
    MovieListRead,
)

router = APIRouter(prefix="/movie_list", tags=["movie_list"])


@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def add_film_to_list(
    movie_in: MovieListCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    existing_movie = crud_movie_list.get_movie_list_by_user_id_and_movie_id(
        db, current_user.id, movie_in.movie_id
    )
    if existing_movie:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Film is already on the list"
        )
    movie_list_in_db = MovieListCreateInDb(
        **jsonable_encoder(movie_in), user_id=current_user.id
    )
    crud_movie_list.create(db=db, obj_in=movie_list_in_db)


@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(
    movie_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    existing_movie = crud_movie_list.get_movie_list_by_user_id_and_movie_id(
        db, current_user.id, movie_id
    )
    if not existing_movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Film is not on the list"
        )

    crud_movie_list.remove(db, existing_movie.id)


@router.get("/list", response_model=list[MovieListRead], status_code=status.HTTP_200_OK)
def read_movie_list(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
) -> list[MovieListRead]:
    movie_list = crud_movie_list.get_movie_list_by_user_id(db, current_user.id)

    if not movie_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="List is empty"
        )

    movies = []
    for movie in movie_list:
        movie_in_db = crud_movie.get(db, movie.movie_id)
        category_name = crud_category.get(db, movie_in_db.category_id).name
        movies.append(
            MovieListRead(
                date_added=str(movie.date_added),
                category_name=category_name,
                **(jsonable_encoder(movie_in_db))
            )
        )

    return movies
