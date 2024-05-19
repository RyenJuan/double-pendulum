# ME5250 Project 2
# Prompt 2: Falling 3R Arm
# Author: Ryan Huang
# Date: 4/21/2024

import matplotlib.pyplot as plt
import numpy as np
import math

'''
Constants
'''
# Gravity
G = 9.8

# Time Step
DT = 0.01

# Iterations
N = 300

# Initial Conditions
pos = [0,0,0]
vel = [0,0,0]
acc = [0,0,0]


def equations(q1, q2, q3, dq1, dq2, dq3, ddq1, ddq2, ddq3):
    """
    :param q1: Link 1 Angle
    :param q2: Link 2 Angle
    :param q3: Link 3 Angle
    :param dq1: Link 1 Angular Velocity
    :param dq2: Link 2 Angular Velocity
    :param dq3: Link 3 Angular Velocity
    :param ddq1: Link 1 Angular Acceleration
    :param ddq2: Link 2 Angular Acceleration
    :param ddq3: Linke 3 Angular Acceleration
    :return: Updated Angular Accelerations
    """
    ddq11 = -1/3 * (-3*G*math.cos(q1) + 2*math.cos(q1 - q2)*ddq2 + math.cos(q1 - q3)*ddq3 - 2*dq1*dq2*math.sin(q2 - q1) -
                   dq1*dq3*math.sin(q3 - q1) - 2*dq2*math.sin(q1 - q2)*(dq1 - dq2) - dq3*math.sin(q1 - q3)*(dq1 - dq3))
    ddq2 = -1 / 2 * (-2 * G * math.cos(q2) + 2 * math.cos(q1 - q2) * ddq1 + math.cos(q2 - q3) * ddq3 - 2 * dq1 * dq2 *
                     math.sin(q1 - q2) - dq2 * dq3 * math.sin(q3 - q2) - 2 * dq1 * math.sin(q1 - q2) * (dq1 - dq2) - dq3
                     * math.sin(q2 - q3) * (dq2 - dq3))
    ddq3 = -1 * (-G * math.cos(q3) + math.cos(q1 - q3) * ddq1 + math.cos(q2 - q3) * ddq2 - dq1 * dq3 * math.sin(
                    q1 - q3) - dq2 * dq3 * math.sin(q2 - q3) - dq1 * math.sin(q1 - q3) * (dq1 - dq3) - dq2 *
                    math.sin(q2 - q3) * (dq2 - dq3))
    return [ddq11,ddq2,ddq3]


def update(accel):
    """
    :param accel: The current accelerations
    :return: Updated Velocities and Positions
    """
    newvel = list(map(lambda x: x * DT, accel))
    newpos = list(map(lambda x: x * DT, vel))

    for i in range(3):
        pos[i] += newpos[i]
        vel[i] += newvel[i]
        acc[i] = accel[i]

    # print(f"Velocities: {vel}")
    print(f"Positions: {pos}")


def plot(save = False):
    """
    Plot the 3R arm
    :return: None
    """
    # Plotting Coordinates of the Link Masses.
    x1 = math.cos(pos[0])
    x2 = math.cos(pos[0]) + math.cos(pos[1])
    x3 = math.cos(pos[0]) + math.cos(pos[1]) + math.cos(pos[2])

    y1 = -math.sin(pos[0])
    y2 = -math.sin(pos[0]) - math.sin(pos[1])
    y3 = -math.sin(pos[0]) - math.sin(pos[1]) - math.sin(pos[2])

    # Plot Parameters
    points = np.array([[0, 0], [x1, y1], [x2, y2], [x3, y3]])
    plt.plot(points[:, 0], points[:, 1], 'ro-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.title('Animation')
    plt.grid(True)
    plt.show()
    plt.close()

    # Save the plot into Frames
    if(save):
        plt.savefig(f'frame {iter}.jpg')


def main():
    for iter in range(N):
        acceleration = equations(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2], acc[0], acc[1], acc[2])
        update(acceleration)
        plot()


if __name__ == "__main__":
    main()