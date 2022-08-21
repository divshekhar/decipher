from ciphers import transpositionCipher
from genetic_algorithm.population import Population
import genetic_algorithm.units as units

class GeneticAlgorithm(object):
    '''
    Genetic Algorithm to find the key of the transposition cipher
    '''

    def __init__(self, population_size: int) -> None:
        self.population_size = population_size
        self.key: str = ""
        self.generation: int = 1

        self.population = Population(self.population_size)
    
    def checkFitnessPlateau(generation_max_fitness: list[float]):
        '''
        Check if the fitness score is plateaued
        '''
        # find frequency of each fitness score
        freq: dict[float, int] = {}

        for fitness in generation_max_fitness:
            # if fitness is not in dictionary,
            # then add it to dictionary with count 1
            if fitness not in freq:
                freq[fitness] = 1
            # if fitness is already in dictionary,
            # then increment count by 1
            else:
                freq[fitness] += 1

        # find max frequency of fitness score
        max_freq: float = max(freq.keys())

        # if max frequency is greater than equal to 50 then we have plateaued
        if freq[max_freq] >= 1000:
            print(freq)
            print(generation_max_fitness)
            return True
        else:
            return False

    def info(self) -> None:
        '''
        Print info about the generation
        '''
        print(
            f"Generation: {self.generation}\tKey: {self.key}\tFitness: {self.population.individuals[0].fitness}")

    def run(self) -> None:
        '''
        Run the genetic algorithm
        '''

        # create initial population
        self.population.initialize()

        while self.generation != 2000:

            # sort the population in decreasing order of fitness score
            self.population.sort()

            # check if the fitness is plateaued
            # if checkFitnessPlateau(self.population.individuals):
            #     break

            # Perform elitism
            self.population.elitism()

            self.key = ''.join(self.population.individuals[0].chromosome)

            self.info()

            self.generation += 1

        self.info()

        # Decrypt Using the key
        decrypt = transpositionCipher.TranspositionCipher().decrypt(units.CIPHER, self.key)
        print(f"Decrypted Text: {decrypt}")
