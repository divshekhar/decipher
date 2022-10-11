import copy
import random
from genetic_algorithm.individual import Individual

class GA(object):
    '''
    Genetic algorithm for breaking transposition cipher
    '''

    def __init__(self, cipher: str, fitness_func: callable, population_size: int, max_generation: int, key_length: int, kmin: int = 1, kmax: int = 9, crossover_rate: float = 0.8) -> None:
        self.cipher = cipher
        self.population_size = population_size
        self.max_generation = max_generation
        self.key_length = key_length
        self.kmin = kmin
        self.kmax = kmax
        self.fitness_func = fitness_func
        self.crossover_rate = crossover_rate
        self.population = [Individual(self.cipher, self.fitness_func, self.key_length) for _ in range(self.population_size)]
        self.best_individual = self.population[0]
    
    def info(self, generation: int, key: str, fitness: float) -> None:
        '''
        print info about the algorithm
        '''
        print(f"Generation = {generation}\t Key = {key}\t Best Fitness = {fitness}")
    
    # crossover function for genetic algorithm
    def crossover(self, parent1: Individual, parent2: Individual) -> Individual:
        '''
        crossover function for genetic algorithm
        '''
        # single point crossover
        child = copy.deepcopy(parent1)

        # crossover point
        crossover_point = random.randint(0, self.key_length - 1)
        # swap values after crossover point
        for i in range(crossover_point, self.key_length):
            key = parent2.key[i]
            while key in child.key:
                key = random.randint(self.kmin, self.kmax)
            child.key[i] = key
        
        return child
    
    # mutate function for genetic algorithm
    def mutate(self, individual: Individual) -> Individual:
        '''
        mutate function for genetic algorithm
        '''
        # swap two random keys
        key1 = random.randint(0, self.key_length - 1)
        key2 = random.randint(0, self.key_length - 1)
        individual.key[key1], individual.key[key2] = individual.key[key2], individual.key[key1]

        return individual
    
    def run(self, log: bool = False) -> Individual:
        '''
        run the genetic algorithm
        '''
        generation = 0
        while generation < self.max_generation:
            # sort the population
            self.population.sort(key=lambda x: x.fitness, reverse=True)
            
            # update the best individual
            if self.population[0].fitness > self.best_individual.fitness:
                self.best_individual = self.population[0]
            
            # print info
            key = ''.join([str(i) for i in self.best_individual.key])

            if log:
                self.info(generation, key, self.best_individual.fitness)

            # create a new population
            new_population: list[Individual] = list()

            # best individual included in new population
            new_population.append(self.best_individual)

            while len(new_population) < self.population_size:
                # select two parents
                parent1 = random.choice(self.population)
                parent2 = random.choice(self.population)
                # crossover
                child = self.crossover(parent1, parent2)
                # mutate
                child = self.mutate(child)
                # evaluate fitness
                child.evaluate_fitness(self.cipher)
                # add child to new population
                new_population.append(child)
            
            # update population
            self.population = new_population
            generation += 1
        
        return self.best_individual