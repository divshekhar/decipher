import copy
import random
from jaya_algorithm.individual import Individual

class JAYA(object):

    def __init__(self, cipher: str, fitness_func: callable, population_size: int, max_iteration: int, key_length: int, kmin: int = 1, kmax: int = 9) -> None:
        self.cipher = cipher
        self.population_size = population_size
        self.max_iteration = max_iteration
        self.key_length = key_length
        self.kmin = kmin
        self.kmax = kmax
        self.fitness_func = fitness_func
        self.population = [Individual(self.cipher, self.fitness_func, self.key_length) for _ in range(self.population_size)]
    
    def sort(self) -> None:
        '''
        sort population by fitness
        '''
        self.population.sort(key=lambda x: x.fitness, reverse=True)
    
    def info(self, iteration: int, key: str, fitness: float) -> None:
        '''
        print info about the algorithm
        '''
        print(f"Iteration = {iteration}\t Key = {key}\t Best Fitness = {fitness}")
    
    def individual_key_opmitization_factor(self, key: int, index: int) -> int:
        r1, r2 = random.randint(0, 4), random.randint(0, 4)
        toward_best_solution = r1 * (self.best_individual.key[index] - key)
        away_from_worst_solution = r2 * (self.worst_individual.key[index] - key)
        return toward_best_solution + away_from_worst_solution
    
    def print_info(self, iteration: int) -> None:
        # Print info every 10 iterations
        if iteration % 10 == 0 and iteration > 1:
            key = "".join([str(i) for i in self.best_individual.key])
            self.info(iteration, key, self.best_individual.fitness)
    
    def run(self, log: bool = False) -> Individual:
        '''
        run jaya algorithm
        '''
        self.sort()
        self.best_individual = self.population[0]
        self.worst_individual = self.population[-1]

        iteration = 0
        while iteration <= self.max_iteration:
            
            for idx in range(self.population_size):
                individual: Individual = copy.deepcopy(self.population[idx])
                updated_individual = copy.deepcopy(individual)

                # update key
                for i in range(-1, self.key_length-1):
                    key: int = abs(individual.key[i] + self.individual_key_opmitization_factor(individual.key[i], i))
                    # Key out of bound condition & key duplication condition
                    while (key < self.kmin or key > self.kmax) or (key in updated_individual.key and key != individual.key[i]):
                        key = random.randint(self.kmin, self.kmax)

                    updated_individual.key[i+1] = key

                # evaluate fitness of updated individual
                updated_individual.evaluate_fitness(self.cipher)

                if updated_individual.fitness > individual.fitness:
                    self.population[idx] = copy.deepcopy(updated_individual)

                # update best and worst individual
                if updated_individual.fitness > self.best_individual.fitness:
                    self.best_individual = copy.deepcopy(updated_individual)
                
                if updated_individual.fitness < self.worst_individual.fitness:
                    self.worst_individual = copy.deepcopy(updated_individual)

            # print info
            if log:
                self.print_info(iteration)
            
            # increment iteration
            iteration += 1
        
        return self.best_individual




                    


