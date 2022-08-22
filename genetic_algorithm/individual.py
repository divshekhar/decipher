from __future__ import annotations
from csv import reader
import random
from ciphers import transpositionCipher
import genetic_algorithm.units as units
import dictionary.fitness as ft


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
    
    def crossover(self, parent2: Individual) -> tuple[Individual, Individual]:
        '''
        Perform single point crossover and produce new offsprings
        '''
        # crossover point
        k = random.randint(1, units.KEY_LENGTH - 1)

        # generate new chromosome for offspring
        child1: list[str] = self.chromosome
        child2: list[str] = parent2.chromosome
        
        child1, child2 = self.generate_unique_child(child1, child2, k)
        
        return Individual(child1), Individual(child2)
    
    def generate_unique_child(self, child1: list[str], child2: list[str], k: int) -> tuple[list[str], list[str]]:
        '''
        Generate unique child
        '''
        root_gene1 = child1[:k]
        root_gene2 = child2[:k]

        rear_gene1 = child1[k:]
        rear_gene2 = child2[k:]

        # if root_gene1 elements are same in rear_gene2, remove those elements
        for gene in root_gene1:
            if gene in rear_gene2:
                rear_gene2.remove(gene)

        # if root_gene2 elements are same in rear_gene1, remove those elements
        for gene in root_gene2:
            if gene in rear_gene1:
                rear_gene1.remove(gene)

        # if root_gene2 elements are not in rear_gene2, add those elements
        for gene in root_gene2:
            if len(root_gene1) + len(rear_gene2) == units.KEY_LENGTH:
                break
            if gene not in rear_gene2 + root_gene1:
                rear_gene2.append(gene)

        # if root_gene1 elements are not in rear_gene1, add those elements
        for gene in root_gene1:
            if len(root_gene2) + len(rear_gene1) == 8:
                break
            if gene not in rear_gene1 + root_gene2:
                rear_gene1.append(gene)

        # combine root_gene1 and rear_gene2
        child1 = root_gene1 + rear_gene2
        child2 = root_gene2 + rear_gene1

        return child1, child2



    def mutate(self) -> None:
        '''
        Perform mutation on individual
        '''
        prob = random.random()
        if (prob < units.MUTATION_RATE):
            idx1: int = random.randint(0, units.KEY_LENGTH - 1)
            idx2: int = random.randint(0, units.KEY_LENGTH - 1)

            # swap both index gene
            self.chromosome[idx1], self.chromosome[idx2] = self.chromosome[idx2], self.chromosome[idx1]

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
        fitness = ft.generateScore(DECRYPT)

        return fitness
    
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
