from ciphers import transpositionCipher
from genetic_algorithm.individual import Individual
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

        self.population = Population(size = self.population_size)
    
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
        individual = self.population.max_fitness_individual
        self.key = ''.join(individual.chromosome)
        print(f"Generation: {self.generation}\tKey: {self.key}\tFitness: {individual.fitness}")

    def run(self) -> None:
        '''
        Run the genetic algorithm
        '''

        # create initial population
        self.population.initialize()

        while self.generation < 500:

            self.population.evaluateFitness() 

            self.population.sort()

            # print
            # if self.generation > 95:
            #     print("Current Population")
            #     for individual in self.population.individuals:
            #         print(individual.chromosome, individual.fitness)

            # crossover
            new_population = self.population.crossover_population()

            # mutate
            new_population.mutate()

            # Perform elitism
            fittest_population: list[Individual] = self.population.elitism()

            # add fittest population to new population
            new_population.individuals.extend(fittest_population)

            # print info
            self.info()
                
            # assign new population
            self.population = new_population

            # if self.generation > 95:
            #     print("New Population")
            #     for individual in self.population.individuals:
            #         print(individual.chromosome, individual.fitness)

            # increment generation
            self.generation += 1
        
        self.population.evaluateFitness()
        self.info()

        # fittest key
        self.key = ''.join(self.population.max_fitness_individual.chromosome)

        # Decrypt Using the key
        decrypt = transpositionCipher.TranspositionCipher().decrypt(units.CIPHER, self.key)
        print(f"\n\nDecryption Key: {self.key} \tfitness: {self.population.max_fitness_individual.fitness}\n")
        print(f"Decrypted Text: {decrypt}\n")
