from __future__ import annotations
import random
from ciphers import transpositionCipher
import dictionary.fitness as fitness
import genetic_algorithm.units as units


class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome: list[str]) -> None:
        self.chromosome = chromosome
        self.fitness: float = self.cal_fitness()

    @classmethod
    def mutated_genes(self) -> str:
        '''
        create random genes for mutation
        '''
        gene: str = random.choice(units.GENES)
        return gene

    @classmethod
    def create_gnome(self) -> list[str]:
        '''
        create chromosome or string of genes
        '''
        gnome: list[str] = []

        # generate key with no repetitions
        while (len(gnome) != units.KEY_LENGTH):
            gene = self.mutated_genes()
            if (gene not in gnome):
                gnome.append(gene)

        return gnome

    def mate(self, parent2: Individual) -> Individual:
        '''
        Perform mating and produce new offspring
        '''
        # chromosome for offspring
        child_chromosome: list[str] = []

        for gp1, gp2 in zip(self.chromosome, parent2.chromosome):

            # random probability
            probability: float = random.random()

            # if probability is less than 0.45, insert gene
            # from parent 1
            if probability < 0.45:
                child_chromosome.append(gp1)

            # if probability is between 0.45 and 0.90, insert
            # gene from parent 2
            elif probability < 0.90:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self) -> float:
        '''
        Calculate fitness score, it is the number of
        characters in string which differ from target
        string.
        '''
        # global TARGET
        fitness: float = 0

        tc = transpositionCipher.TranspositionCipher()
        key = ''.join(self.chromosome)

        # Decrypt cipher using key
        DECRYPT: str = tc.decrypt(units.CIPHER, key)

        # Calculate fitness score
        fitness = fitness.generateScore(DECRYPT)

        return fitness
