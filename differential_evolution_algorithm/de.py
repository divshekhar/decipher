import copy
import random
from differential_evolution_algorithm.individual import Individual

class DE(object):
    '''
    Differential Evolution Algorithm
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
    
    # mutant function for differential evolution algorithm
    def mutant(self, a: Individual, b: Individual, c: Individual) -> Individual:
        '''
        mutant function for differential evolution algorithm
        '''
        mutant: Individual = copy.deepcopy(a)
        for i in range(self.key_length):
            key = b.key[i] + (c.key[i] - a.key[i])
            if (key < self.kmin or key > self.kmax):
                while key in mutant.key:
                    if random.random() < 0.5:
                        key = random.choice(b)
                    else:
                        key = random.choice(c)
        
        return mutant

    
    # trial function for differential evolution algorithm
    def trial(self, mutant: Individual) -> Individual:
        '''
        trial function for differential evolution algorithm
        '''
        trial: Individual = copy.deepcopy(mutant)
        for i in range(self.key_length):
            if random.random() < 0.5:
                key = random.randint(self.kmin, self.kmax)
                while key in trial.key:
                    key = random.randint(self.kmin, self.kmax)
                trial.key[i] = key

        return trial
    
    # crossover function for differential evolution algorithm
    def crossover(self, a: Individual) -> Individual:
        '''
        crossover function for differential evolution algorithm
        '''
        b: Individual = random.choice(self.population)
        crossover: Individual = copy.deepcopy(a)
        for i in range(self.key_length):
            key = a.key[i]
            while key in crossover.key:
                key = random.randint(self.kmin, self.kmax)
            crossover.key[i] = key

        return crossover
    
    def run(self, log: bool = False) -> Individual:
        '''
        run differential evolution algorithm
        '''
        generation = 1
        while generation <= self.max_generation:
            
            for i in range(self.population_size):

                # select 3 random individuals
                while True:
                    a, b, c = random.sample(self.population, 3)
                    if a != b and b != c and c != a:
                        break
                
                # create mutant
                mutant = self.mutant(a, b, c)
                # if generation < 2 or generation > 98:
                #     print(f"Generation = {generation}\t mutant = {mutant.key}")
                
                # create trial
                trial = self.trial(mutant)
                # if generation < 2 or generation > 98:
                #     print(f"Generation = {generation}\t trial = {trial.key}")

                # create crossover
                crossover = self.crossover(trial)
                if random.random() < self.crossover_rate:
                    trial = crossover
                # if generation < 2 or generation > 98:
                #     print(f"Generation = {generation}\t crossover = {trial.key}")
                
                # change crossover_rate after every generation
                # CR(min) = 0.5
                # CR(max) = 0.9
                # CR = CR(min) + (generation * (CR(max) - CR(min)) / max_generation)
                self.crossover_rate = 0.5 + (generation * ((0.9 - 0.5) / self.max_generation))
                
                # evaluate fitness of trial
                trial.evaluate_fitness(self.cipher)
                
                # replace individual with trial if trial is better
                if trial.fitness > self.population[i].fitness:
                    self.population[i] = trial
                
                # update best individual
                if trial.fitness > self.best_individual.fitness:
                    self.best_individual = trial
            
            # print info about the algorithm
            if log:
                key = "".join([str(i) for i in self.best_individual.key])
                self.info(generation, key, self.best_individual.fitness)
            
            # increment generation
            generation += 1
        
        return self.best_individual
    