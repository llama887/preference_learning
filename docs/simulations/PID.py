import matplotlib.pyplot as plt
plt.ion()
import math
from naive import Agent, naive_control

def PID(agent, previous_error=0, total_error=0):
    agent.x += math.sin(agent.heading)
    agent.y += math.cos(agent.heading)
    reference = 0
    error = reference - agent.x
    total_error += error
    k_p_= 0.1
    k_i_= 0.005
    k_d_= 0.3

    control_signal = k_p_ * error + k_i_ * total_error + k_d_ * (error - previous_error)
    agent.heading += control_signal
    if agent.heading > math.pi/2:
        agent.heading = math.pi/2
    if agent.heading < -math.pi/2:
        agent.heading = -math.pi/2
    
    agent.positions_x.append(agent.x)
    agent.positions_y.append(agent.y)
    return agent, previous_error, total_error
    


def main():
    naive_agent = Agent()
    PID_agent = Agent()
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
    previous_error=0
    total_error=0
    while naive_agent.y < 100 or PID_agent.y < 100:
        ax.clear()
        ax.plot(x_point, y_point, 'go')
        ax.plot(x_line, y_line, color='black')
        plt.plot([], [], color=naive_agent.color, label='Naive Agent')
        plt.plot([], [], color=PID_agent.color, label='PID Agent')
        plt.legend()

        
        if naive_agent.y < 100:
            naive_agent = naive_control(naive_agent)
        ax.scatter(naive_agent.positions_x, naive_agent.positions_y, color=naive_agent.color)
        if PID_agent.y < 100:
            PID_agent, previous_error, total_error = PID(PID_agent, previous_error=previous_error, total_error=total_error)
        ax.scatter(PID_agent.positions_x, PID_agent.positions_y, color=PID_agent.color)
        ax.set_aspect('equal', adjustable='datalim')
        ax.axis('off')
        plt.draw()
        plt.pause(0.01)

    plt.pause(10)

if __name__ == "__main__":
    main()  