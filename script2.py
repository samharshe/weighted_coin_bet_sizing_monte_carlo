import random
import numpy as np
import matplotlib.pyplot as plt

def flip_coin(weight):
    return random.random() < weight

def calculate_new_pot(old_pot, bet, weight):
    return old_pot * (1 + bet) if flip_coin(weight) else (old_pot * (1 - bet))

outputs = open('outputs.txt', 'w')

weights = np.arange(0.5, 1.0, 0.05).tolist()
bets = np.arange(0.0, 1.0, 0.005).tolist()

for weight in weights:
    returns = []
    for bet in bets:
        pot = 1.0
        for i in range(10000):
            if pot <= 0.01:
                pot = 0
                break
            if pot >= 100:
                pot = 100
                break
            else: 
                pot = calculate_new_pot(pot, bet, weight)
        returns.append(pot)
        outputs.write(f"Ending value: {round(pot, 4)}\n")
        outputs.write(f"Bet size: {round(bet, 3)}\n")
        outputs.write(f"Coin weight: {round(weight, 3)}\n")
        outputs.write("-"*20)
        outputs.write("\n")

    plt.scatter(bets, returns)
    plt.title(f"Bet size v. returns for coin weight {round(weight, 2)}")
    plt.show()