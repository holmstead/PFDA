# Simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.

import numpy as np

# define the army size
attacker_troops = 3
defender_troops = 2

print(f"Battle starts with {attacker_troops} attackers and {defender_troops} defenders.")

# create a die roling function
def roll_dice(num_rolls=1):
    """
    Roll a die a specified number of times.
    """
    # Generate random integers between 1 and 6 (inclusive)
    rolls = np.random.randint(1, 7, size=num_rolls)
    return rolls


# attacker rolls the dice
attacker_rolls = roll_dice(3)  # roll the dice 3 times
print(f"\nAttacker rolls: {attacker_rolls}")

# defender rolls the dice
defender_rolls = roll_dice(2)  # roll the dice 2 times
print(f"Defender rolls: {defender_rolls}")

max_attacker = np.max(attacker_rolls)

print(f"\nMax roll from attacker = {max_attacker}")


max_defender = np.max(defender_rolls)

print(f"Max roll from defender = {max_defender}")

if max_attacker == max_defender:
    attacker_troops -= 1
    print("\nTie: Attacker loses 1 troop.")
elif max_attacker < max_defender:
    attacker_troops -= 1
    print("\nAttacker loses: Attacker loses 1 troop.")
elif max_attacker > max_defender:
    defender_troops -= 1
    print("\nAttacker wins: Defender loses 1 troop.")

print(f"\nAttacker has {attacker_troops} soldiers left")
print(f"Defender has {defender_troops} soldiers left")