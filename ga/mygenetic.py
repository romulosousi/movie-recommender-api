

from ga.algorithm import Algorithm
from sqlalchemy.orm import Session
from fastapi import Depends
import numpy as np
import math 

from db.database import get_db
from db.repositories import MovieRepository, RatingsRepository

class MyGeneticAlgorithm(Algorithm):

    def __init__(self, individual_size, population_size, p_crossover, p_mutation, total_items, max_generations=100, size_hall_of_fame=1, fitness_weights=(1.0, ), seed=42, db=None) -> None:


        super().__init__(
            individual_size, 
            population_size, 
            p_crossover, 
            p_mutation, 
            total_items, 
            max_generations, 
            size_hall_of_fame, 
            fitness_weights, 
            seed)
        
        self.db = db

    
    def evaluate(self, individual):

        if len(individual) != len(set(individual)):
            return (0.0, )
        
        ratings_movies = RatingsRepository.find_by_movieid_list(self.db, individual)
        
        mean_ = np.mean([obj_.rating for obj_ in ratings_movies])

        if math.isnan(mean_):
            mean_ = 0.0

        return (mean_, )


if __name__ == "__main__":



    genetic = MyGeneticAlgorithm(10, 100, 0.9, 0.05, 400)
    genetic.eval()

