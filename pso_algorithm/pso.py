from pso_algorithm.particle import Particle

class PSO(object):

    def __init__(self, cipher: str, fitness: callable, swarm_size: int, max_iteration: int, key_length: int, min_velocity: float = -4, max_velocity: float = 4.0) -> None:

        # PSO Parameters
        self.w: float = 0.729 # Inertia Weight

        # Acceleration parameters
        self.c1: float = 1.49445 # Self-Confidence
        self.c2: float = 1.49445 # Swarm-Confidence

        self.cipher = cipher
        self.max_iteration = max_iteration
        self.fitness = fitness
        self.swarm_size = swarm_size
        self.key_length = key_length
        self.swarm = [Particle(self.cipher, self.fitness, self.key_length) for _ in range(self.swarm_size)]
        
        # Initialize pbest & gbest
        self.pbest: Particle = self.swarm[0]
        self.gbest: Particle = self.swarm[0]

        for particle in self.swarm:
            if particle.fitness > self.pbest.fitness:
                self.pbest = particle

            if particle.fitness > self.gbest.fitness:
                self.gbest = particle
    
    def info(self, iteration: int, key: str, fitness: float) -> None:
        # print info about the algorithm
        print(f"Iteration = {iteration}\t Key = {key}\t Best Fitness = {fitness}")

    def run(self, log: bool = False) -> Particle:
        # run pso algorithm

        iteration = 0
        while iteration <= self.max_iteration:

            # Print info every 10 iterations
            if log and (iteration % 10 == 0 and iteration > 1):
                key = "".join([str(i) for i in self.gbest.key])
                self.info(iteration, key, self.gbest.fitness)

            for particle in self.swarm:
                # Update velocity
                particle.update_velocity(self.w, self.c1, self.c2, self.pbest, self.gbest)
                # Update position
                particle.update_position()

                # update pbest if the particle has a better fitness than the current pbest
                if particle.fitness > self.pbest.fitness:
                    self.pbest = particle

                # update gbest if the particle has a better fitness than the current gbest
                if particle.fitness > self.gbest.fitness:
                    self.gbest = particle
            
            # shift position
            for _ in range(self.key_length):
                position_shifted_particle = self.gbest.random_shift_position()
                if position_shifted_particle.fitness > self.gbest.fitness:
                    self.gbest = position_shifted_particle
            
            # increment iteration
            iteration += 1
        
        return self.gbest
