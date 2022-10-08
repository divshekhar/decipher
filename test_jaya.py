import time
from ciphers import transpositionCipher
from jaya_algorithm.individual import Individual
from jaya_algorithm.jaya import JAYA
from dictionary.fitness import generateScore

CIPHER: str = '''ic eotadt ii g,etoisqf kw pb nt neeBmlsnareedd ropdawuhslernnnettl n neraldsynro neihelcoeThsewrflditkotlenirlte mollehdn ys shf fmenfgaoihtogtabtrato mnror  hfl ufasesejfshf asuo-isvyxm swefe lhs  ,y  tctuh a fg.ocso ta nvtc die t.e cdvlnkcnl nn i,tou  cpcsaimmkaecseoasrnt ik p nlf_Tnuedbi pdihttilath cii e getcicc ro  rawaora pcaasnyh t suoheon lts lialu   gaibg oen hp hn noyoe viesiig.nedi vpblas eya ,cuoatf rd  tcmohwuilahkr mao efatre ltein liaeu euirstswt,e   ach  amliemt  fi ytceosio _d smws nny dn tw  hiietr r-oeo tonr  a ohellen,a  nv acdiheaeegs aaweir'''.replace("_", " ")

key_length = 8
population_size = 100
max_iteration = 500

print("\nBegin JAYA for finding transposition cipher key\n")
print("Setting num_particles = " + str(population_size))
print("Setting max_iterarion = " + str(max_iteration))
print("\n-------------Starting JAYA algorithm-------------\n")

# start clock
start_time = time.time()
jaya = JAYA(CIPHER, generateScore, population_size, max_iteration, key_length)
best_individual: Individual = jaya.run()
# end clock
end_time = time.time()

key = "".join([str(i) for i in best_individual.key])

print("\n-------------JAYA algorithm completed-------------\n")
print("\nBest Key Found:")

# Decrypt the ciphertext using the key found by PSO
decrypt = transpositionCipher.TranspositionCipher().decrypt(CIPHER, key)
print(f"\n\nDecryption Key: {key} \tfitness: {best_individual.fitness}\n")
print(f"Decrypted Text: {decrypt}\n")

# Print the time taken to run the algorithm
print(f"Execution time of the algorithm: {end_time - start_time} seconds")
