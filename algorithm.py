from __future__ import annotations

from genetic_algorithm.ga import GA
from pso_algorithm.pso import PSO
from jaya_algorithm.jaya import JAYA
from differential_evolution_algorithm.de import DE
from enhanced_jaya_algorithm.ejaya import EnhancedJAYA

from dictionary.fitness import generateScore

class Algorithm:
    GA = 1
    PSO = 2
    JAYA = 3
    DE = 4
    EJAYA = 5

    @staticmethod
    def get_algo(algo: Algorithm) -> str:
        if algo == Algorithm.GA:
            return "GA"
        elif algo == Algorithm.PSO:
            return "PSO"
        elif algo == Algorithm.JAYA:
            return "JAYA"
        elif algo == Algorithm.DE:
            return "DE"
        elif algo == Algorithm.EJAYA:
            return "EJAYA"
        else:
            return "Unknown"
    
    # return algoritm object
    @staticmethod
    def get_algo_obj(algo: Algorithm, cipher: str,population_size: int, max_iteration: int, key_length: int) -> object:
        if algo == Algorithm.GA:
            return GA(cipher,generateScore,population_size,max_iteration,key_length)
        elif algo == Algorithm.PSO:
            return PSO(cipher,generateScore,population_size,max_iteration,key_length)
        elif algo == Algorithm.JAYA:
            return JAYA(cipher,generateScore,population_size,max_iteration,key_length)
        elif algo == Algorithm.DE:
            return DE(cipher,generateScore,population_size,max_iteration,key_length)
        elif algo == Algorithm.EJAYA:
            return EnhancedJAYA(cipher,generateScore,population_size,max_iteration,key_length)
        else:
            return None