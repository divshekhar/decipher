# Genetic Algorithm

Breaking transposition cipher usign Genetic Algorithm attack.

## Steps:

### 1. Initialize initial population

Create initial population from the genes. No duplicate genes in an individual's chromosome.

### 2. Calculate fitness of the population

Fitness evaluation is done for every individual in the population

### 3. Population crossover

Single point crossover is done on parents choosen by tournament selection.

Tournament Selection: Best parents are selected for the tournament, from half of the original population

Crossover for unique keys:
Note: If two parents with same chromosomes comes for crossover, children with random genes will be created.

Steps:
1. First crossover is done on the crossover point generated randomly
2. Then from the rear end of the genes similar keys are removed
3. Root genes are added back to the rear genes to complete the genes
4. unique genes is obtained

### 4. Mutation

Swap mutation is done on the crossovered population

### 5. Elitism

10% of the fittest population is added to the new population.
Similar keys are not included.

