import time
from algorithm import Algorithm
from ciphers.transpositionCipher import TranspositionCipher
from key import random_key
from plain_text import get_plain_text

# Change algorithms
# algo: Algorithm = Algorithm.GA
# algo: Algorithm = Algorithm.PSO
# algo: Algorithm = Algorithm.JAYA
algo: Algorithm = Algorithm.DE
algo_str: str = Algorithm.get_algo(algo)

key_length = 8
population_size = 100
max_iteration = 100
cipher_length = 500

text = get_plain_text(cipher_length)
encryption_key = ''.join(str(k) for k in random_key(key_length))

# convert text to cipher
CIPHER = TranspositionCipher().encrypt(text, encryption_key)

print(f"\nBegin {algo_str} for finding transposition cipher key\n")
print("Parameters:")
print("**************************************")
print(f"key length: {key_length}")
print(f"cipher length: {cipher_length}")
print(f"population_size: {population_size}")
print(f"max_iteration {max_iteration}")
print("**************************************")
print(f"\n-------------Starting {algo_str} algorithm-------------\n")

algo_obj = Algorithm.get_algo_obj(algo, CIPHER, population_size, max_iteration, key_length)

# start clock
start_time = time.time()
best_individual = algo_obj.run(log = True)
# end clock
end_time = time.time()

decryption_key = "".join([str(i) for i in best_individual.key])

print(f"\n-------------{algo_str} algorithm completed-------------\n")
print(f"Encryption Key {encryption_key}")
print("\nBest Key Found:")

# Decrypt the ciphertext using the key found by PSO
decrypt = TranspositionCipher().decrypt(CIPHER, decryption_key)
print(f"\nDecryption Key: {decryption_key} \tfitness: {best_individual.fitness}\n")
print(f"Decrypted Text: {decrypt}\n")

# Print the time taken to run the algorithm
print(f"Execution time of the {algo_str} algorithm: {end_time - start_time} seconds\n")
