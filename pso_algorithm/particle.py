from __future__ import annotations
from ciphers import transpositionCipher
import copy
import random

class Particle(object):
    def __init__(self, cipher: str, fitness_func: callable, key_length: int, kmin: int = 1, kmax: int = 9, vmax: float = 4, vmin: float = -4) -> None:

        self.cipher = cipher
        self.kmin = kmin
        self.kmax = kmax
        self.vmax = vmax
        self.vmin = vmin
        self.fitness_func = fitness_func
        self.fitness: float = 0.0

        # initialize position of the particle
        self.key: list[int] = list()
        while len(self.key) < key_length:
            k: int = random.randint(kmin, kmax)
            if k not in self.key:
                self.key.append(k)
        
        # initialize velocity of the particle
        self.velocity: list[float] = [((vmax - vmin) * random.random() + vmin) for _ in range(key_length)]

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
    
    
    def update_velocity(self, w: float, c1: float, c2: float, pbest: Particle, gbest: Particle) -> None:
        '''
        Update velocity of particle
        '''

        for i in range(len(self.velocity) - 1):
            r1 = random.random()
            r2 = random.random()
            
            # Formula
            # self.velocity[i+1] = self.velocity[i] + c1 * r1 * (pbest.position[i] - self.position[i]) + c2 * r2 * (gbest.position[i] - self.position[i])

            cognitive_velocity: float = c1 * r1 * (pbest.key[i] - self.key[i])
            social_velocity: float = c2 * r2 * (gbest.key[i] - self.key[i])
            self.velocity[i + 1] = (w * self.velocity[i]) + cognitive_velocity + social_velocity

    
    def update_position(self) -> None:
        '''
        Update position of particle
        '''
        
        for i in range(len(self.key) - 2):
            # new key = old key + velocity
            new_key = int(self.key[i] + self.velocity[i])
            # check if new key is within bounds
            if new_key > self.kmax or new_key < self.kmin:
                # create new key within bounds
                key = random.randint(self.kmin, self.kmax)
                # check if new key is already in key
                while key in self.key:
                    key = random.randint(self.kmin, self.kmax)
                # update key
                new_key = key
        
            self.key[i+1] = new_key
        
        # Evaluate fitness of the particle
        self.evaluate_fitness(self.cipher)
    
    def random_shift_position(self) -> Particle:
        '''
        Shift position of particle
        '''

        particle = copy.copy(self)
        position = particle.key

        # shift position
        offset: int = random.randint(2, len(position) - 2)
        
        # circular shift position
        particle.key = position[offset:] + position[:offset]
        
        # Evaluate fitness of the particle
        particle.evaluate_fitness(self.cipher)

        return particle
    
    def left_shift_position(self, offset: int) -> Particle:
        '''
        Shift position of particle
        '''

        particle = copy.copy(self)
        position = particle.key

        # circular shift position
        particle.key = position[offset:] + position[:offset]
        
        # Evaluate fitness of the particle
        particle.evaluate_fitness(self.cipher)

        return particle