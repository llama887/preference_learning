import matplotlib.pyplot as plt
plt.ion()
import random
import math
from naive import Agent, naive_control

class Open_Loop_Agent(Agent):
    def __init__(self):
        super().__init__()
        self.heading = 0

def open_loop_control(agent):
    agent.x += math.sin(agent.heading)
    agent.y += math.cos(agent.heading)
    agent.positions_x.append(agent.x)
    agent.positions_y.append(agent.y)
    print(agent.y)
    return agent

def disturbance(agent):
    agent.x += (random.random() - 0.3)*2
    agent.y += (random.random() - 0.5)*2
    agent.heading += (random.random() - 0.3)*0.05
    return agent

def main():
    naive_agent = Agent()
    open_loop_agent = Open_Loop_Agent()
    fig, ax = plt.subplots()

    # target position
    x_point, y_point = 0, 100
    x_line, y_line = [0, x_point], [0, y_point]
    ax.plot(x_point, y_point, 'go')

    # Plot the ideal path
    ax.plot(x_line, y_line, color='black')
    ax.axis('off')

    ax.set_aspect('equal', adjustable='datalim')
    starting_position = Agent()
    plt.plot(starting_position.x, starting_position.y, 'ro') # plot a red dot to show where agents start
    while naive_agent.y < 100 or open_loop_agent.y < 100:
        ax.clear()
        ax.plot(x_point, y_point, 'go')
        ax.plot(x_line, y_line, color='black')
        if naive_agent.y < 100:
           naive_agent = naive_control(naive_agent)
        ax.scatter(naive_agent.positions_x, naive_agent.positions_y, color=naive_agent.color)
        if open_loop_agent.y < 100:
            open_loop_agent = open_loop_control(open_loop_agent)
        ax.scatter(open_loop_agent.positions_x, open_loop_agent.positions_y, color=open_loop_agent.color)

        if random.random() < 0.1:
            naive_agent = disturbance(naive_agent)
            open_loop_agent = disturbance(open_loop_agent)
        ax.set_aspect('equal', adjustable='datalim')
        ax.axis('off')
        plt.draw()
        plt.pause(0.01)

    plt.pause(10)

if __name__ == "__main__":
    main()  