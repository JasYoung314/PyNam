"""
Script for all the plots for the talk
"""
import random
import matplotlib.pyplot as plt, mpld3

def walk(number_of_walks):
    """
    Simulate people walking along the pavement K times
    """
    player_1 = [random.choice('LR') for k in range(number_of_walks)]
    player_2 = [random.choice('LR') for k in range(number_of_walks)]
    impacts = sum([player_1[k] == player_2[k] for
                                       k in range(number_of_walks)])
    return impacts
fig = plt.figure()
plt.hist([walk(500) for k in range(1000)])
plt.xlabel('Number of impacts')
plt.ylabel('Frequency')
mpld3.save_html(fig,"random_choice.html", d3_url='./js/d3.js', mpld3_url='./js/mpld3.js')
