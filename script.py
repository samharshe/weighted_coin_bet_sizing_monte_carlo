import random
import numpy as np

def flip_coin(weight):
    return random.random() < weight

def calculate_new_pot_size(old_pot_size, bet_proportion, weight):
    return old_pot_size * (1 + bet_proportion) if flip_coin(weight) else (old_pot_size * (1 - bet_proportion))

outputs = open('outputs.txt', 'w')

weights = np.arange(0.5, 1.0, 0.005).tolist()
bet_proportions = np.arange(0, 1.0, 0.005).tolist()

for weight in weights:
    for proportion in bet_proportions:
        pot_size = 1
        for i in range(1000):
            if pot_size <= 0.01:
                pot_size = 0
                break
            if pot_size >= 100:
                pot_size = 100
                break
            else: 
                pot_size = calculate_new_pot_size(pot_size, proportion, weight)

        outputs.write(f"Ending value: {round(pot_size, 4)}\n")
        outputs.write(f"Bet proportion: {round(proportion, 3)}\n")
        outputs.write(f"Coin weight: {round(weight, 3)}\n")
        outputs.write("-"*20)
        outputs.write("\n")
        pot_size = 1