from typing import List
from sqlalchemy.orm import Session 

from db.models import Movie, Ratings, User

class MovieRepository:

    @staticmethod
    def find_all(db: Session) -> List[Movie]:
        return db.query(Movie).all()
    
    @staticmethod
    def find_by_id(db: Session, id: int) -> Movie:
        return db.query(Movie).filter(Movie.movieId == id).first()
    
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Movie).filter(Movie.movieId == id).first() is not None
    

class UserRepository:

    @staticmethod
    def find_all(db: Session) -> List[User]:
        return db.query(User).all()
    
    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.userId == id).first()
    
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.userId == id).first() is not None
    

class RatingsRepository:

    @staticmethod
    def find_by_userid(db: Session, id: int) -> List[Ratings]:
        return db.query(Ratings).filter(Ratings.userId == id).all()
    
    @staticmethod
    def find_by_movieid(db: Session, id: int) -> List[Ratings]:
        return db.query(Ratings).filter(Ratings.movieId == id).all()