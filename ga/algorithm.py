
from deap import base, algorithms, creator, tools
import random
import numpy as np

class Algorithm:

    def __init__(self, individual_size, population_size, p_crossover, p_mutation,  all_ids, max_generations=100, size_hall_of_fame=1, fitness_weights=(1.0,), seed=42) -> None:

        self.POPULATION_SIZE = population_size
        self.P_CROSSOVER = p_crossover
        self.P_MUTATION = p_mutation
        self.MAX_GENERATIONS = max_generations
        self.HALL_OF_FAME_SIZE = size_hall_of_fame
        self.RANDOM_SIZE = seed

        random.seed(seed)

        creator.create("FitnessMax", base.Fitness, weights=fitness_weights)
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self.toolbox = base.Toolbox()

        self.toolbox.register("attribute", random.choice, all_ids)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attribute, individual_size)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", self.evaluate)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        self.population = self.toolbox.population(n=population_size)
        self.hall_of_fame = tools.HallOfFame(self.HALL_OF_FAME_SIZE)
        self.statistics = tools.Statistics(lambda ind: ind.fitness.values)
        self.statistics.register("avg", np.mean)
        self.statistics.register("std", np.std)
        self.statistics.register("min", np.min)
        self.statistics.register("max", np.max)


    def evaluate(self):
        pass 

    def eval(self):
        self.population, self.log = algorithms.eaSimple(
            self.population, 
            self.toolbox, 
            cxpb=self.P_CROSSOVER,
            mutpb=self.P_MUTATION,
            ngen=self.MAX_GENERATIONS,
            stats=self.statistics,
            halloffame=self.hall_of_fame,
            verbose=True)

    def get_population(self):
        return self.population
    
    def get_log(self):
        return self.log

    def get_best(self):
        return self.hall_of_fame[0]
        



        
        