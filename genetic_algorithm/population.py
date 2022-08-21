import random
from genetic_algorithm.individual import Individual

class Population(object):
    '''
    Class representing population of individuals
    '''

    def __init__(self, size: int) -> None:
        self.size: int = size

        self.individuals: list[Individual] = []
        self.generation: int = 1
        self.max_fitness: float = 0

    def initialize(self) -> None:
        '''
        Initialize population with individuals
        '''
        for _ in range(self.size):
            gnome = Individual.create_gnome()
            self.individuals.append(Individual(gnome))
    
    def evaluateFitness(self) -> None:
        '''
        Evaluate fitness of each individual in population
        '''
        for individual in self.individuals:
            individual.fitness = individual.cal_fitness()
            if individual.fitness > self.max_fitness:
                self.max_fitness = individual.fitness
    
    def sort(self) -> None:
        '''
        Sort individuals in population according to fitness score (descending order)
        '''
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)
    
    def elitism(self) -> None:
        '''
        Perform elitism, keep top 1% of individuals in population
        '''
        new_generation: list[Individual] = []
        new_generation = self.individuals[:int(self.size * 1/100)]

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((99*self.size)/100)
        for _ in range(s):
            parent1 = random.choice(self.individuals[:50])
            parent2 = random.choice(self.individuals[:50])
            child: Individual = parent1.mate(parent2)
            new_generation.append(child)

        self.individuals = new_generation