import random
import numpy as np
import matplotlib.pyplot as plt

def calculate_new_pot(old_pot, bet, weight):
    return old_pot * (1 + bet) if random.random() < weight else old_pot * (1 - bet)

outputs = open('outputs2.txt', 'w')

weights = np.arange(0.5, 1.0, 0.025).tolist()
bets = np.arange(0.005, 1.0, 0.005).tolist()
least_rounds = []

for weight in weights:
    average_rounds = []
    for bet in bets:
        rounds = []
        for i in range(100):
            pot = 1.0
            for j in range(10000):
                if pot >= 2:
                    rounds.append(j)
                    break
                elif pot <= 0.01:
                    rounds.append(10000)
                    break
                else: 
                    pot = calculate_new_pot(pot, bet, weight)
            if pot < 2:
                rounds.append(10000)
        average_rounds.append(sum(rounds)/len(rounds))
    
    least_rounds.append(bets[average_rounds.index(min(average_rounds))])
    
    plt.scatter(bets, average_rounds)
    plt.title(f"Bet size v. average number of rounds to double for coin weight {round(weight, 3)}")
    plt.show()

plt.scatter(weights, least_rounds)
plt.plot([0.5, 1], [0, 1])
plt.title(f"Coin weight v. bet size at which the pot took the least number of rounds to double")
plt.show()