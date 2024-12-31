# Research Track I - Second Assignment Part II
This repository contains the assignment work for the **Research Track I** course, completed by:  
**Rubin Khadka Chhetri**  
**ID: 6558048**

## Table of Contents
- [Introduction](#introduction)
- [Node Details](#node-details)
    - [Robot Controller Node](#robot-controller-node-robot_controller)
- [Repository Structure](#repository-structure)
- [Getting Started (Read Before Action)](#getting-started-read-before-action)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
- [Launching Nodes](#launching-nodes)
- [Implementation Details](#implementation-details)
- [Summary](#summary)

## Introduction

This repository contains a ROS2 package designed to control a robot in a simulation environment. It implements a single main node:
**Robot Controller Node**. 

The robot is pre-spawned at position `(2, 2)` by another package. The goal of this package is to move the robot by publishing velocity commands to the `/cmd_vel` topic. 

This package demonstrates the use of ROS2 to enable basic robot motion control and interaction with the simulation environment.

**Note**:
- This assignment is completed using both **Python** and **C++**. 

## Node Details

### Robot Controller Node (robot_controller)
The **Robot Controller Node** is responsible for controlling the robot's movements in the simulation based on user input. It handles both linear and angular velocity commands and interacts with the robot via the `/cmd_vel` topic.

**Key Functions**:
 - **User Input Handling**: The node prompts the user to input values for the robot's linear and angular velocities.
 - **Movement Execution**: After the velocities are set, the node sends the corresponding movement commands to the robot, causing it to move for one second.
 - **Stop and Reset**: After one second of movement, the robot stops, and the interface is reset, allowing the user to input new movement commands.

## Repository Structure

The root of this repository is the package folder, which contains all necessary files and scripts for running the assignment nodes. When cloning the repository for the first time, place it directly in the `src` folder of your ROS2 workspace.

### Folder and File Overview
- **`/assignment2_rt_part2`**: Contains the main package for controlling the robot in the simulation.
    - `__init__.py`: Initializes the package for Python.
    - `robot_controller.py`: Contains the logic for handling user input and controlling the robot’s movement.

- **`/resource`**: Holds any additional resources or configuration files needed for the package.
    - `assignment2_rt_part2`:  Configuration or resource-related files for the package.

- **`/test`**: Includes test scripts for verifying the package’s functionality and code quality.
    - `test_copyright.py`: Ensures compliance with copyright requirements.
    - `test_flake8.py`: Validates Python code style using flake8.
    - `test_pep257.py`: Ensures adherence to PEP 257 docstring conventions.

- **`/setup.py`**: The script to build and install the package.

- **`/setup.cfg`**: Configuration file for packaging and distributing the package.

- **`/package.xml`**: Lists dependencies and package metadata.

- **`/README.md`**: This file (Documentation).

## Getting Started (Read Before Action)

### Prerequisites
Before proceeding, ensure that **`ROS2`** is installed on your system.
This package has been developed with **ROS2 Foxy**, but it should work with other ROS2 versions as well. 

If you haven’t set up ROS2 yet, you can follow the official guide to install it:
[ROS2 Installation Guide][https://docs.ros.org/]

Additionally, you’ll need **`Python 3`** package to run this project. Ensure it is installed on your system. If not, you can install it by running:
```bash
sudo apt-get update
sudo apt-get install python3
```
After installation, you can proceed to settting up the workspace.

### Setup

## Launching Nodes
## Implementation Details
## Summary
