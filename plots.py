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
    player_1 = [random.choice('LR') for k in range(number_of_walks)]
    player_2 = [random.choice('LR') for k in range(number_of_walks)]
    impacts = sum([player_1[k] != player_2[k] for
                                       k in range(number_of_walks)])
    return impacts

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=20)
plt.xlabel('Number of impacts')
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
    player_1 = [random.choice('L') for k in range(number_of_walks)]
    player_2 = [random.choice('L') for k in range(number_of_walks)]
    impacts = sum([player_1[k] != player_2[k] for
                                       k in range(number_of_walks)])
    return impacts

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=1)
plt.xlabel('Number of impacts')
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
    player_1 = [random.choice('L') for k in range(number_of_walks)]
    player_2 = [random.choice('R') for k in range(number_of_walks)]
    impacts = sum([player_1[k] != player_2[k] for
                                       k in range(number_of_walks)])
    return impacts

fig = plt.figure()
plt.hist([walk(500) for k in range(1000)], bins=1)
plt.xlabel('Number of impacts')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times but all walking on the same side')
plt.xlim(0,505)
mpld3.save_html(fig,"left_right.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')

# Script for 'left_right.html'
# What if everyone walks on opposite sides
strategy_1 = (20,80)  # Walk on the Left 20 out of 100 times
strategy_2 = (90,10)  # Walk on the left 50 out of 100 times

def walk(number_of_walks=500, strategy_1=(1,1), strategy_2=(1,1)):
    """
    Simulate people walking along the pavement K times
    """
    player_1 = [random.choice('L' * strategy_1[0] + 'R' * strategy_1[1])
                                             for k in range(number_of_walks)]
    player_2 = [random.choice('L' * strategy_2[0] + 'R' * strategy_2[1])
                                             for k in range(number_of_walks)]
    impacts = sum([player_1[k] != player_2[k] for
                                       k in range(number_of_walks)])
    return impacts

fig = plt.figure()
plt.hist([walk(500, strategy_1, strategy_2) for k in range(1000)], bins=20)
plt.xlabel('Number of impacts')
plt.ylabel('Frequency')
plt.title('Simulating 2000 people walking towards each other 500 times but mixing things up')
plt.xlim(0,505)
mpld3.save_html(fig,"mixed.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')
