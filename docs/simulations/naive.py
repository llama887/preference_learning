import matplotlib.pyplot as plt
plt.ion()
import random
import math

fig, ax = plt.subplots()

# target position
x_point, y_point = 0, 100
x_line, y_line = [0, x_point], [0, y_point]
ax.plot(x_point, y_point, 'go')

# Plot the ideal path
ax.plot(x_line, y_line, color='black')
ax.axis('off')

ax.set_aspect('equal', adjustable='datalim')

class Agent:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.positions_x = [self.x]
        self.positions_y = [self.y]
        self.color = (random.random(), random.random(), random.random())
        self.heading = (random.random() - 0.5) * 3
starting_position = Agent()
plt.plot(starting_position.x, starting_position.y, 'ro') # plot a red dot to show where agents start

def naive_control(agent):
    agent.x += math.sin(agent.heading)
    agent.y += math.cos(agent.heading)
    reference = 0
    error = reference - agent.x
    K_ = 0.1
    control_signal = K_ * error
    agent.heading += control_signal

    #print(agent.x, agent.y)
    agent.positions_x.append(agent.x)
    agent.positions_y.append(agent.y)
    return agent

naive_agent = Agent()
while naive_agent.y < 100:
    ax.clear()
    ax.plot(x_point, y_point, 'go')
    ax.plot(x_line, y_line, color='black')
    
    naive_agent = naive_control(naive_agent)
    ax.scatter(naive_agent.positions_x, naive_agent.positions_y, color=naive_agent.color)
    ax.set_aspect('equal', adjustable='datalim')
    ax.axis('off')
    plt.draw()
    plt.pause(0.01)

plt.pause(10)