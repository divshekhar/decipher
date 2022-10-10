from __future__ import annotations
import random
from ciphers import transpositionCipher

class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, cipher: str, fitness: callable, key_length: int, kmin: int = 1, kmax: int = 9) -> None:
        
        self.cipher = cipher
        self.kmin = kmin
        self.kmax = kmax
        self.fitness_func = fitness

        # initialize position of the particle
        self.key: list[int] = list()
        while len(self.key) < key_length:
            k: int = random.randint(kmin, kmax)
            if k not in self.key:
                self.key.append(k)
        
        # Evaluate fitness of the particle
        self.evaluate_fitness(self.cipher)
    
    def evaluate_fitness(self, cipher: str) -> None:
        '''
        Evaluate fitness of the particle
        '''
        key = "".join([str(i) for i in self.key])
        tc = transpositionCipher.TranspositionCipher()
        plaintext = tc.decrypt(cipher, key)
        self.fitness = self.fitness_func(plaintext)