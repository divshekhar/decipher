from __future__ import annotations
import random
from genetic_algorithm.individual import Individual

class Population(object):
    '''
    Class representing population of individuals
    '''

    def __init__(self, individuals: list[Individual] = [], size: int = 100) -> None:
        self.individuals = [*set(individuals)]

        if len(self.individuals) == 0:
            self.size = size
        else:
            self.size = len(individuals)

        self.generation: int = 1
        self.max_fitness_individual: Individual = Individual([])

    def initialize(self, genes: str, key_length: int) -> None:
        '''
        Initialize population with individuals
        '''

        self.individuals = [Individual(Individual.create_gnome(genes, key_length)) for _ in range(self.size)]

    
    def evaluateFitness(self, cipher: str) -> None:
        '''
        Evaluate fitness of each individual in population
        '''

        for individual in self.individuals:
            individual.fitness = individual.cal_fitness(cipher)
            if individual.fitness > self.max_fitness_individual.fitness:
                self.max_fitness_individual = individual
    
    def sort(self) -> None:
        '''
        Sort individuals in population according to fitness score (descending order)
        '''

        self.individuals.sort(key=lambda x: x.fitness, reverse=True)
    
    def tournament_selection(self) -> tuple[Individual, Individual]:
        '''
        Tournament selection
        parents size = population size / 2
        returns best two individuals from tournament
        '''

        parents = self.individuals[:int(self.size/2)]
        return random.choice(parents), random.choice(parents)
    
    def crossover_population(self, genes: str, key_length: int, randomness_rate: float = 0.5) -> Population:
        '''
        Crossover population
        '''

        new_generation: list[Individual] = []
        for i in range(int(self.size/2)):
            parent1, parent2 = self.tournament_selection()
            child1,child2 = parent1.crossover(parent2, genes, key_length, randomness_rate)

            new_generation.append(child1)
            new_generation.append(child2)
        
        return Population(individuals=new_generation)

    
    # Mutate population
    def mutate(self, genes: str, key_length: int, rate: float) -> None:
        '''
        Mutate population by swaping genes
        '''
        for individual in self.individuals:
            individual.mutate(genes, key_length, rate)

    def elitism(self) -> list[Individual]:
        '''
        Perform elitism, keep top 2% of the fittest individuals from the population
        '''
        
        elites: set[Individual] = set()

        size = int(self.size * 2/100)

        for individual in self.individuals:
            elites.add(individual)
            
            if len(elites) == size:
                break

        return elites
            