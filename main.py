from typing import List, Union
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session 

from db.models import Movie
from db.database import engine, Base, get_db
from db.repositories import MovieRepository, UserRepository, RatingsRepository
from db.schemas import MovieRequest, MovieResponse, UserRequest, UserResponse, RatingsResponse, RatingsRequest

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Genetic Algorithm Movie Recommender API",
    description="An API to recommeder movies using genetic algorithm approach",
    version="0.0.1",
    terms_of_service=None,
    contact=None,
    license_info=None
)

@app.get("/api/movies", response_model=List[MovieResponse],
         name="Get all movies",
         description="Return all movies from database.")
def find_all_movies(db: Session = Depends(get_db)):
    movies = MovieRepository.find_all(db)
    return [MovieResponse.from_orm(movie) for movie in movies]


@app.get("/api/movies/{id}", response_model=MovieResponse,
         name="Get movie by id",
         description="Return a especific movie by id.")
def find_movie_by_id(id: int, db: Session = Depends(get_db)):
    movie = MovieRepository.find_by_id(db, id)

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found."
        )
    
    return MovieResponse.from_orm(movie)

@app.get("/api/users", response_model=List[UserResponse],
         name="Get all users",
         description="Return all users from database.")
def find_all_users(db: Session = Depends(get_db)):
    users = UserRepository.find_all(db)

    return [UserResponse.from_orm(user) for user in users]

@app.get("/api/users/{id}", response_model=UserResponse,
         name="Get user by id",
         description="Return a especific user by id.")
def find_user_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.find_by_id(db, id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    
    return UserResponse.from_orm(user)


@app.get("/api/movies_by_user/{user_id}", response_model=List[RatingsResponse],
         name="Get all movies rated by user",
         description="Return all movies that was rated by a user with the rating.")
def find_movies_by_user(user_id: int, db: Session = Depends(get_db)):

    ratings = RatingsRepository.find_by_userid(db, user_id)
    
    if len(ratings) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    
    return [RatingsResponse.from_orm(rating) for rating in ratings]


@app.get("/api/users_by_movie/{movie_id}", response_model=List[RatingsResponse],
         name="Get all users that rated a movie",
         description="Return all users that rated a movie with the rating.")
def find_users_by_movie(movie_id: int, db: Session = Depends(get_db)):

    ratings = RatingsRepository.find_by_movieid(db, movie_id)
    
    if len(ratings) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found."
        )
    
    return [RatingsResponse.from_orm(rating) for rating in ratings]


@app.get("/api/recommender/{user_id}",
         name="Get a recommendation for a user.",
         description="Create a recommendation for a especific user.")
def get_recommender(user_id: int, db: Session = Depends(get_db)):

    return "Not implemented yet"


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)