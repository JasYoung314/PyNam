"""
Script for all the plots for the talk
"""
import random
import matplotlib.pyplot as plt, mpld3

# Script for 'random_choice.html'
# A plot of people randomly bumping in to each other
def walk(number_of_walks):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('LR') for k in range(number_of_walks)]
    blues = [random.choice('LR') for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=20)
plt.xlabel('Number of bumps')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times randomly')
plt.xlim(0,500)
mpld3.save_html(fig,"random_choice.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'all_left.html'
# What if everyone walks on the left?
def walk(number_of_walks):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('L') for k in range(number_of_walks)]
    blues = [random.choice('L') for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=1)
plt.xlabel('Number of bumps')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times but all agreeing on a side')
plt.xlim(-5,500)
mpld3.save_html(fig,"all_left.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'left_right.html'
# What if everyone walks on opposite sides
def walk(number_of_walks):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('L') for k in range(number_of_walks)]
    blues = [random.choice('R') for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=1)
plt.xlabel('Number of bumps')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times but all walking on the same side')
plt.xlim(0,505)
mpld3.save_html(fig,"left_right.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'mixed.html'
# What if everyone walks on opposite sides
red_strategy = (20,80)  # Walk on the Left 20 out of 100 times
blue_strategy = (90,10)  # Walk on the left 50 out of 100 times

def walk(number_of_walks=500, red_strategy=(1,1), blue_strategy=(1,1)):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('L' * red_strategy[0] + 'R' * red_strategy[1])
                                             for k in range(number_of_walks)]
    blues = [random.choice('L' * blue_strategy[0] + 'R' * blue_strategy[1])
                                             for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.hist([walk(500, red_strategy, blue_strategy) for k in range(1000)], bins=20)
plt.xlabel('Number of bumps')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times but mixing things up')
plt.xlim(0,505)
mpld3.save_html(fig,"mixed.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'effect_against_left.html'
# What if everyone walks on opposite sides

def walk(number_of_walks=500, red_strategy=(1,1), blue_strategy=(1,1)):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('L' * red_strategy[0] + 'R' * red_strategy[1])
                                             for k in range(number_of_walks)]
    blues = [random.choice('L' * blue_strategy[0] + 'R' * blue_strategy[1])
                                             for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.scatter(range(100), [walk(10000, (1,0), (x, 100-x)) for x in range(100)])
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('The effect of x (proportion of time walking left) against people walking left')
plt.xlim(0,100)
plt.ylim(0,10000)
mpld3.save_html(fig,"effect_against_left.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'effect_against_half_and_half.html'

def walk(number_of_walks=500, red_strategy=(1,1), blue_strategy=(1,1)):
    """
    Simulate people walking along the pavement K times
    """
    reds = [random.choice('L' * red_strategy[0] + 'R' * red_strategy[1])
                                             for k in range(number_of_walks)]
    blues = [random.choice('L' * blue_strategy[0] + 'R' * blue_strategy[1])
                                             for k in range(number_of_walks)]
    bumps = sum([reds[k] != blues[k] for
                                       k in range(number_of_walks)])
    return bumps

fig = plt.figure()
plt.scatter(range(100), [walk(10000, (1,1), (x, 100-x)) for x in range(100)])
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('The effect of x (proportion of time walking left) against people walking randomly')
plt.xlim(0,100)
plt.ylim(0,10000)
mpld3.save_html(fig,"effect_against_half_and_half.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'evolutionary dynamics'

# Evolutionary dynamics with both starting on the left
size_of_population = 100
number_of_rounds = 500
death_rate = .05
reds = ['L' for k in range(size_of_population)]
blues = ['L' for k in range(size_of_population)]
red_data = [sum([k == 'L' for k in reds])]
blue_data = [sum([k == 'L' for k in reds])]
for rnd in range(number_of_rounds):
    for indx, pair in enumerate(zip(reds, blues)):
        if pair[0] != pair[1]:
            if random.random() < death_rate:
                reds[indx], blues[indx] = blues[indx], reds[indx]
    red_data.append(sum([k == 'L' for k in reds]))
    blue_data.append(sum([k == 'L' for k in blues]))

fig = plt.figure()
plt.scatter(range(len(red_data)), red_data, color='red', marker='>')
plt.scatter(range(len(blue_data)), blue_data, color='blue', marker='<')
plt.xlabel('round')
plt.ylabel('Number of the left')
plt.title('Start with same convention')
plt.ylim(0,101)
plt.xlim(0, number_of_rounds)
mpld3.save_html(fig,"evolutionary_dynamics_both_L.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Evolutionary dynamics with both starting on a given side
size_of_population = 100  # Number of people
number_of_rounds = 500  # How many rounds
death_rate = .05  # Chance of mind change

reds = [random.choice('LR') for k in range(size_of_population)]
blues = [random.choice('LR') for k in range(size_of_population)]
red_data = [sum([k == 'L' for k in reds])]
blue_data = [sum([k == 'L' for k in reds])]

for rnd in range(number_of_rounds):  # Loop through rounds
    for j, pair in enumerate(zip(reds, blues)):  # Loop through players
        if pair[0] != pair[1]:  # If bump
            if random.random() < death_rate:  # If mind change
                reds[j], blues[j] = blues[j], reds[j]
    red_data.append(sum([k == 'L' for k in reds]))  # Data collection
    blue_data.append(sum([k == 'L' for k in blues]))

fig = plt.figure()
plt.scatter(range(len(red_data)), red_data, color='red', marker='>')
plt.scatter(range(len(blue_data)), blue_data, color='blue', marker='<')
plt.xlabel('round')
plt.ylabel('Number of the left')
plt.title('Start with different conventions')
plt.ylim(0,101)
plt.xlim(0, number_of_rounds)
mpld3.save_html(fig,"evolutionary_dynamics_L_and_R.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')


# Evolutionary dynamics with a mutation rate:
# Evolutionary dynamics
size_of_population = 100  # Number of people
number_of_rounds = 500  # How many rounds
mutation_rate = .05  # Chance of changing strategy
death_rate = .05  # Chance of mind change

reds = ['L' for k in range(size_of_population)]
blues = ['L' for k in range(size_of_population)]
red_data = [sum([k == 'L' for k in reds])]
blue_data = [sum([k == 'L' for k in reds])]

for rnd in range(number_of_rounds):  # Loop through rounds
    for j, pair in enumerate(zip(reds, blues)):  # Loop through players

        if random.random() < mutation_rate:  # Check if random change
            reds[j], blues[j] = random.choice('LR'), random.choice('LR')

        if pair[0] != pair[1]:  # If bump
            if random.random() < death_rate:  # If mind change
                reds[j], blues[j] = blues[j], reds[j]

    red_data.append(sum([k == 'L' for k in reds]))  # Data collection
    blue_data.append(sum([k == 'L' for k in blues]))

fig = plt.figure()
plt.scatter(range(len(red_data)), red_data, color='red', marker='>')
plt.scatter(range(len(blue_data)), blue_data, color='blue', marker='<')
plt.xlabel('round')
plt.ylabel('Number of the left')
plt.title('Start with same conventions but random mutation')
plt.ylim(0,101)
plt.xlim(0, number_of_rounds)
mpld3.save_html(fig, "evolutionary_dynamics_L_and_R_with_mutation.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')
