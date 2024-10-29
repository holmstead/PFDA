# Simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.

import numpy as np
import matplotlib.pyplot as plt
import time

# create a die roling function
def roll_dice(num_rolls=1):
    """
    Roll a die a specified number of times.
    """
    # create a random number generator without a fixed seed
    rng = np.random.default_rng()
    
    # Generate random integers between 1 and 6 (inclusive)
    rolls = rng.integers(1, 7, size=num_rolls)
    return rolls

def check_winner(attacker_number, defender_number):
    '''
    Function takes in two numbers and checkes who wins, and who loses troops
    '''
    attacker_losses = 0
    defender_losses = 0
    if attacker_number > defender_number:
        #print(f"Attackers {attacker_number} beats defenders {defender_number}")
        defender_losses += 1 
        #print("Defender loses 1 troop.")
    elif attacker_number < defender_number:
        #print(f"Defenders {defender_number} beats attackers {attacker_number}")
        attacker_losses += 1
        #print("Attacker loses 1 troop.")
    elif attacker_number == defender_number:
        #print(f"Attackers {attacker_number} vs defenders {defender_number}")
        attacker_losses += 1
        #print("Tie: Attacker loses 1 troop.")
    return attacker_losses, defender_losses

# now do 1000 battles
print(r"""                                                                                                
                   L E T   T H E   B A T T L E   B E G I N !
""")

time.sleep(1)
print("\t**carnage ensues**")
time.sleep(3)

# initialise variables to count total losses
total_attacker_losses = 0
total_defender_losses = 0

# define how many round to play
number_of_rounds = 1000

# start the loop
for i in range(number_of_rounds):
    #print(f"\nRound {i+1}")
    # attacker rolls the dice
    attacker_rolls = roll_dice(3)  # roll the dice 3 times
    #print(f"\nAttacker rolls: {attacker_rolls}")

    # defender rolls the dice
    defender_rolls = roll_dice(2)  # roll the dice 2 times
    #print(f"Defender rolls: {defender_rolls}")

    # sort the lists in descending order (highest to lowest)
    sorted_attacker = np.sort(attacker_rolls)[::-1]
    sorted_defender = np.sort(defender_rolls)[::-1]

    # print the soretd lists to see whats going on
    #print(f"\tAttacker rolls (sorted): {sorted_attacker}")
    #print(f"\tDefender rolls (sorted): {sorted_defender}")

    # compare highest die value
    attacker_number = sorted_attacker[0]
    defender_number = sorted_defender[0]
    attacker_losses, defender_losses = check_winner(attacker_number, defender_number)
    
    # add the losses to the total
    total_attacker_losses += attacker_losses
    total_defender_losses += defender_losses
    

    # compare second highest die value
    attacker_number = sorted_attacker[1]
    defender_number = sorted_defender[1]
    attacker_losses, defender_losses = check_winner(attacker_number, defender_number)
    
    # add the losses to the total
    total_attacker_losses += attacker_losses
    total_defender_losses += defender_losses

    #print(f"total attacker losses: {total_attacker_losses}")
    #print(f"total defender losses: {total_defender_losses}")


print(f"\nTotal attacker losses: {total_attacker_losses}")
print(f"Total defender losses: {total_defender_losses}")


if total_attacker_losses > total_defender_losses:
    print(f"\n\tOuch, the Attacker has suffered heavy losses")
else:
    print(f"\n\tOuch, the Defender has suffered heavy losses")

# plot the results
losses = [total_attacker_losses, total_defender_losses]
labels = ["Total Attacker Losses", "Total Defender Losses"]

# Set up the canvas
fig, ax = plt.subplots()

# create the pie chart with an explode effect
explode = [0.02, 0]  # Explode the first slice (attacker losses), no explode for the second slice
ax.pie(losses, labels=labels, autopct='%1.1f%%', startangle=140, 
       colors=['yellow', 'blue'], explode=explode, shadow=True)

# decorate plot
ax.set_title(f"Comparison of Losses - {number_of_rounds} rounds")

# display the plot
plt.tight_layout()
plt.show()