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
        key: set[int] = set()
        while len(key) < key_length:
            key.add(random.randint(kmin, kmax))
        
        self.position: list[int] = list(key)

        # initialize velocity of the particle
        self.velocity: list[float] = [((vmax - vmin) * random.random() + vmin) for _ in range(key_length)]

        # Evaluate fitness of the particle
        self.evaluate_fitness(self.cipher)
    
    def evaluate_fitness(self, cipher: str) -> None:
        '''
        Evaluate fitness of the particle
        '''
        key = "".join([str(i) for i in self.position])
        tc = transpositionCipher.TranspositionCipher()
        plaintext = tc.decrypt(cipher, key)
        self.fitness = self.fitness_func(plaintext)
    
    
    def update_velocity(self, w: float, c1: float, c2: float, pbest: Particle, gbest: Particle) -> None:
        '''
        Update velocity of particle
        '''

        for i in range(len(self.velocity)):
            r1 = random.random()
            r2 = random.random()
            cognitive_velocity: float = c1 * r1 * (pbest.position[i] - self.position[i])
            social_velocity: float = c2 * r2 * (gbest.position[i] - self.position[i])
            self.velocity[i] = (w * self.velocity[i]) + cognitive_velocity + social_velocity
    
    def update_position(self) -> None:
        '''
        Update position of particle
        '''
        
        # for i in range(len(self.position)):
        #     self.position[i] = int(self.position[i] + self.velocity[i])
        #     if self.position[i] > self.kmax:
        #         self.position[i] = self.kmax
        #     if self.position[i] < self.kmin:
        #         self.position[i] = self.kmin

        
        # Evaluate fitness of the particle
        self.evaluate_fitness(self.cipher)
    
    def shift_position(self, shift: int) -> Particle:
        '''
        Shift position of particle
        '''

        particle = copy.copy(self)
        position = particle.position
        
        # circular shift position
        particle.position = position[shift:] + position[:shift]
        
        # Evaluate fitness of the particle
        particle.evaluate_fitness(self.cipher)

        return particle