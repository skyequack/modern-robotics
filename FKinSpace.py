#program to calculate the end effector configuration of a robot with 6 degrees of freedom. change values of theta, M, and screw_axes.
#screw axes can be calculated using screw-axis-calculator.py

import numpy as np
import modern_robotics as mr

def main():
    # Define the screw axes
    screw_axes = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

    # Define joint variable values (in radians)
    theta = np.array([np.pi, np.pi, np.pi, -np.pi, 1, np.pi])

    # Define the home configuration (optional if not provided by default)
    M = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

    # Compute the forward kinematics using FKinSpace
    T = mr.FKinSpace(M, screw_axes, theta)

    # Print the resulting end-effector configuration with 2 decimal places
    print("End-effector configuration:")
    np.set_printoptions(precision=2, suppress=True)
    print(T)

if __name__ == "__main__":
    main()
