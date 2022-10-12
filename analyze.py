import time
from algorithm import Algorithm
from ciphers.transpositionCipher import TranspositionCipher

from plain_text import get_plain_text
from key import random_key

CIPHER_LENGTHS = [100, 500, 1000, 2000]
KEY_LENGTHS = [5, 6, 7, 8]
POPULATION_SIZES = [10, 50, 100]
MAX_ITERATIONS = [100, 200, 300, 400, 500]
MEAN_VALUE = 3

def cipher_length_vs_execution_time(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"CIPHER LENGTH VS EXECUTION TIME ({algo_str})")
    print("-------------------------------------")

    global CIPHER_LENGTHS

    # parameters
    population_size = 100
    max_iteration = 100
    key_length = 8

    key = ''.join(str(k) for k in random_key(key_length))

    for cipher_length in CIPHER_LENGTHS:

        # Encrypt the plaintext using the key
        text = get_plain_text(cipher_length)
        cipher = TranspositionCipher().encrypt(text, key)

        execution_time_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            # start clock
            start_time = time.time()
            algo_obj.run()
            # end clock
            end_time = time.time()

            # calculate time taken
            time_taken = end_time - start_time
            execution_time_list.append(time_taken)

        execution_time = sum(execution_time_list) / len(execution_time_list)

        print(f"Cipher length: {cipher_length}")
        print("----------------------------")
        print(f"Execution Time = {execution_time}")
        print("----------------------------")

def key_length_vs_execution_time(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"KEY LENGTH VS EXECUTION TIME ({algo_str})")
    print("-------------------------------------")

    global KEY_LENGTHS

    # parameters
    population_size = 100
    max_iteration = 100
    cipher_length = 500

    text = get_plain_text(cipher_length)
    
    for key_length in KEY_LENGTHS:

        # create random key of length key_length
        key = ''.join(str(k) for k in random_key(key_length))
        # Encrypt the plaintext using the key
        cipher = TranspositionCipher().encrypt(text, key)

        execution_time_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            # start clock
            start_time = time.time()
            algo_obj.run()
            # end clock
            end_time = time.time()

            # calculate time taken
            time_taken = end_time - start_time
            execution_time_list.append(time_taken)

        execution_time = sum(execution_time_list) / len(execution_time_list)

        print(f"Key length: {key_length}")
        print("----------------------------")
        print(f"Execution Time = {execution_time}")
        print("----------------------------")

def population_size_vs_execution_time(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"POPULATION SIZE VS EXECUTION TIME ({algo_str})")
    print("-------------------------------------")

    global POPULATION_SIZES

    # parameters
    max_iteration = 100
    cipher_length = 500
    key_length = 8

    text = get_plain_text(cipher_length)

    # create random key of length key_length
    key = ''.join(str(k) for k in random_key(key_length))
    # Encrypt the plaintext using the key
    cipher = TranspositionCipher().encrypt(text, key)

    for population_size in POPULATION_SIZES:

        execution_time_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            # start clock
            start_time = time.time()
            algo_obj.run()
            # end clock
            end_time = time.time()

            # calculate time taken
            time_taken = end_time - start_time
            execution_time_list.append(time_taken)

        execution_time = sum(execution_time_list) / len(execution_time_list)

        print(f"Population Size: {population_size}")
        print("----------------------------")
        print(f"Execution Time = {execution_time}")
        print("----------------------------")

def max_iteration_vs_execution_time(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"MAX ITERATION VS EXECUTION TIME ({algo_str})")
    print("-------------------------------------")

    global MAX_ITERATIONS

    # parameters
    population_size = 100
    cipher_length = 500
    key_length = 8

    text = get_plain_text(cipher_length)
    key = random_key(key_length)

    key = ''.join(str(k) for k in key)
    # Encrypt the plaintext using the key
    cipher = TranspositionCipher().encrypt(text, key)

    for max_iteration in MAX_ITERATIONS:

        execution_time_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            # start clock
            start_time = time.time()
            algo_obj.run()
            # end clock
            end_time = time.time()

            # calculate time taken
            time_taken = end_time - start_time
            execution_time_list.append(time_taken)

        execution_time = sum(execution_time_list) / len(execution_time_list)

        print(f"Max Iteration: {max_iteration}")
        print("----------------------------")
        print(f"Execution Time = {execution_time}")
        print("----------------------------")

def cipher_length_vs_accuracy(algo: Algorithm):
    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"CIPHER LENGTH VS ACCURACY ({algo_str})")
    print("-------------------------------------")

    global CIPHER_LENGTHS

    # parameters
    population_size = 100
    max_iteration = 100
    key_length = 8

    key = ''.join(str(k) for k in random_key(key_length))

    for cipher_length in CIPHER_LENGTHS:

        text = get_plain_text(cipher_length)

        # Encrypt the plaintext using the key
        cipher = TranspositionCipher().encrypt(text, key)

        correct_characters_list: list[int] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            best_individual = algo_obj.run()

            # Decrypt the ciphertext using the key
            key = "".join([str(i) for i in best_individual.key])
            decrypt = TranspositionCipher().decrypt(cipher, key)

            # count no. of correct characters
            correct = 0
            for i in range(len(text)):
                if text[i] == decrypt[i]:
                    correct += 1

            # calculate accuracy
            correct_characters_list.append(correct)

        correct_characters = sum(correct_characters_list) / len(correct_characters_list)
        accuracy = (correct_characters / cipher_length) * 100 

        print(f"Cipher length: {cipher_length}")
        print("----------------------------")
        print(f"Correct characters: {correct_characters}")
        print(f"Accuracy = {accuracy}%")
        print("----------------------------")

def population_size_vs_accuracy(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"POPULATION SIZE VS ACCURACY ({algo_str})")
    print("-------------------------------------")

    global POPULATION_SIZES

    # parameters
    max_iteration = 100
    cipher_length = 500
    key_length = 8

    text = get_plain_text(cipher_length)

    key = ''.join(str(k) for k in random_key(key_length))
    # Encrypt the plaintext using the key
    cipher = TranspositionCipher().encrypt(text, key)

    for population_size in POPULATION_SIZES:

        correct_characters_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            best_individual = algo_obj.run()

            # Decrypt the ciphertext using the key
            key = "".join([str(i) for i in best_individual.key])
            decrypt = TranspositionCipher().decrypt(cipher, key)

            # count no. of correct characters
            correct = 0
            for i in range(len(text)):
                if text[i] == decrypt[i]:
                    correct += 1

            # calculate accuracy
            correct_characters_list.append(correct)

        correct_characters = sum(correct_characters_list) / len(correct_characters_list)
        accuracy = (correct_characters / cipher_length) * 100 

        print(f"Population Size: {population_size}")
        print("----------------------------")
        print(f"Correct characters: {correct_characters}")
        print(f"Accuracy = {accuracy}%")
        print("----------------------------")

def max_iteration_vs_accuracy(algo: Algorithm):

    # identify the algorithm
    algo_str: str = Algorithm.get_algo(algo)
    print(f"MAX ITERATION VS ACCURACY ({algo_str})")
    print("-------------------------------------")

    global MAX_ITERATIONS

    # parameters
    population_size = 100
    cipher_length = 500
    key_length = 8

    text = get_plain_text(cipher_length)
    key = random_key(key_length)
    
    key = ''.join(str(k) for k in random_key(key_length))
    # Encrypt the plaintext using the key
    cipher = TranspositionCipher().encrypt(text, key)

    for max_iteration in MAX_ITERATIONS:

        correct_characters_list: list[float] = list()

        for _ in range(3):

            # create algorithm object
            algo_obj = Algorithm.get_algo_obj(algo, cipher, population_size, max_iteration, key_length)
            best_individual = algo_obj.run()

            # Decrypt the ciphertext using the key
            key = "".join([str(i) for i in best_individual.key])
            decrypt = TranspositionCipher().decrypt(cipher, key)

            # count no. of correct characters
            correct = 0
            for i in range(len(text)):
                if text[i] == decrypt[i]:
                    correct += 1

            # calculate accuracy
            correct_characters_list.append(correct)

        correct_characters = sum(correct_characters_list) / len(correct_characters_list)
        accuracy = (correct_characters / cipher_length) * 100 

        print(f"Max Iteration: {max_iteration}")
        print("----------------------------")
        print(f"Correct characters: {correct_characters}")
        print(f"Accuracy = {accuracy}%")
        print("----------------------------")

if __name__ == "__main__":
    algo: Algorithm = Algorithm.PSO

    cipher_length_vs_execution_time(algo)
    # key_length_vs_execution_time(algo)
    # population_size_vs_execution_time(algo)
    # max_iteration_vs_execution_time(algo)
    # population_size_vs_accuracy(algo)
    # max_iteration_vs_accuracy(algo)
    # cipher_length_vs_accuracy(algo)
