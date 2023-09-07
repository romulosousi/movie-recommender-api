from db.database import engine, Base, get_db
from db.database import SessionLocal
from sqlalchemy.orm import Session 
from db.models import Movie

from imdb import Cinemagoer

cine = Cinemagoer()

db = SessionLocal()

all_movies = db.query(Movie).all()
total = len(all_movies)
count = 1
for movie in all_movies:
    print("%i -> %i/%i" % (movie.movieId,count ,total))
    if movie.url_poster == '':

        try:
            movie_search = cine.get_movie(movie.imdbId)
            cover_url = movie_search['cover url']

            movie.url_poster = cover_url
        except Exception as e:
            print("Erro no filme " + str(movie.movieId))
    
    if count % 10 == 0:
        db.commit()

    count += 1

    





