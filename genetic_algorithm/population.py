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

    def initialize(self) -> None:
        '''
        Initialize population with individuals
        '''

        s = 0

        while s < self.size:
            gnome = Individual.create_gnome()
            individual = Individual(gnome)
            self.individuals.append(individual)

            # remove duplicate keys from the initial population
            self.individuals = [*set(self.individuals)]
            s = len(self.individuals)

    
    def evaluateFitness(self) -> None:
        '''
        Evaluate fitness of each individual in population
        '''

        for individual in self.individuals:
            individual.fitness = individual.cal_fitness()
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

        parents = random.choices(self.individuals, k=int(self.size/2))
        parents.sort(key=lambda x: x.fitness, reverse=True)
        return parents[0], parents[1]
    
    def crossover_population(self) -> Population:
        '''
        Crossover population
        '''

        new_generation: list[Individual] = []
        for i in range(int(self.size/2)):
            parent1, parent2 = self.tournament_selection()
            child1,child2 = parent1.crossover(parent2)

            new_generation.append(child1)
            new_generation.append(child2)

        return Population(new_generation)
    
    # Mutate population
    def mutate(self) -> None:
        '''
        Mutate population by swaping genes
        '''
        for individual in self.individuals:
            individual.mutate()

    def elitism(self) -> list[Individual]:
        '''
        Perform elitism, keep top 10% of the fittest individuals from the population
        '''

        elites: set[Individual] = set()

        size = int(self.size * 10/100)

        for individual in self.individuals:
            elites.add(individual)
            
            if len(elites) == size:
                break

        return elites

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        # s = int((99*self.size)/100)
        # for _ in range(s):
        #     parent1 = random.choice(self.individuals[:50])
        #     parent2 = random.choice(self.individuals[:50])
        #     child: Individual = parent1.mate(parent2)
        #     new_generation.append(child)

        # self.individuals = new_generation
            