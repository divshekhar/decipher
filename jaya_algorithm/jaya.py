from ast import Pass
import random
from re import S
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
        r1, r2 = random.randint(self.kmin, self.kmax), random.randint(self.kmin, self.kmax)
        toward_best_solution = r1 * (self.best_individual.key[index] - key)
        away_from_worst_solution = r2 * (self.worst_individual.key[index] - key)
        return toward_best_solution + away_from_worst_solution
    
    def run(self) -> Individual:
        '''
        run jaya algorithm
        '''
        self.sort()
        self.best_individual = self.population[0]
        self.worst_individual = self.population[-1]

        iteration = 0
        while iteration <= self.max_iteration:

            # Print info every 10 iterations
            if iteration % 10 == 0 and iteration > 1:
                key = "".join([str(i) for i in self.gbest.position])
                self.info(iteration, key, self.gbest.fitness)
            
            for individual in self.population:

                for i in range(self.key_length - 1):
                    key: int = individual.key[i] + self.individual_key_opmitization_factor(individual.key[i], i)
                    # conditions
                    out_of_bound_condition: bool = key > self.kmax or key < self.kmin
                    key_duplication_condition: bool = (key not in individual.key) and (key != individual.key[i + 1])
                    while out_of_bound_condition:
                        key = random.randint(self.kmin, self.kmax)
                        print("Inhere key", key)
                    
                    individual.key[i + 1] = key

                print(individual.key)
                individual.evaluate_fitness(self.cipher)

            self.sort()
            self.best_individual = self.population[0]
            self.worst_individual = self.population[-1]

            iteration += 1
        
        return self.best_individual




                    


