import random
print("Random number:", random.randint(1, 100))

random_list = [random.randint(1, 100) for _ in range(5)]
print("Random list:", random_list)

random.shuffle(random_list)
print("Shuffled list:", random_list)