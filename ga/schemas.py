

from pydantic import BaseModel


class GeneticConfiguration(BaseModel):
    query_search: int = 1
    individual_size: int = 10
    population_size: int = 100
    p_crossover: float = 95
    p_mutation: float = 5
    max_generations: int = 30
    size_hall_of_fame: int = 1
    seed: int = 42