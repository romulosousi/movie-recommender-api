
from deap import base, algorithms, creator, tools

class Algorithm:

    def __init__(self, individual_size, population_size, p_crossover, p_mutation, max_generation=100, fitness_weights=(1.0,)) -> None:

        creator.create("FitnessMax", base.Fitness, weights=fitness_weights)
        creator.create("Individual", list, typecode='int', fitness=creator.FitnessMax)

        self.toolbox = base.Toolbox()

        self.toolbox.register("")

        
        