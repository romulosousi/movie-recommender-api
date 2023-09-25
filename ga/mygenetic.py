

from ga.algorithm import Algorithm
from sqlalchemy.orm import Session
from fastapi import Depends
import numpy as np
import math 

from db.database import get_db
from db.repositories import UserRepository, MovieRepository, RatingsRepository

class MyGeneticAlgorithm(Algorithm):

    def __init__(self, query_search, individual_size, population_size, p_crossover, p_mutation, all_ids, max_generations=100, size_hall_of_fame=1, fitness_weights=(1.0, ), seed=42, db=None) -> None:


        super().__init__(
            individual_size, 
            population_size, 
            p_crossover, 
            p_mutation, 
            all_ids, 
            max_generations, 
            size_hall_of_fame, 
            fitness_weights, 
            seed)
        
        self.db = db
        self.all_ids = all_ids
        self.query_search = query_search
        

    


def evaluate_recomendacao(self, individual, user_ratings):

    if len(individual) != len(set(individual)):
        return (0.0, )
    
    if len(list(set(individual) - set(self.all_ids))) > 0:
        return (0.0, )

    ratings_movies = RatingsRepository.find_by_movieid_list(self.db, individual)

    if len(ratings_movies) > 0:
        mean_ = np.mean([obj_.rating for obj_ in ratings_movies])
    else:
        mean_ = 0.0


    user_mean = np.mean(user_ratings)
