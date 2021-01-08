## Overview
In this project, a basic planner functionlaity is provisioned for navigating (orientating) the turtlebot to Northstar (Polaris). We are using Turtlebot3 for the robot and Gazebo for the simulation. 

## Authors

- [Vinayak Ravi](https://github.com/vinayakravi14)

## Dependencies

- Ubuntu 16.04/18.04/20.4 ((Tested with Noetic))
- ROS Kinetic (Note: If you are using Noetic, you will have to proceed with ROS Noetic)
- Gazebo
- Turtlebot3 Packages (turtlebot3, turtlebot3_msgs, turtlebot3_simulations, turtlebo_interactions)
- Python Packages:  Math, Queue

## Run Instructions

- Clone the repository in your ROS workspace. Type
```
cd ~/<ROS_Workspace>/src
git clone https://github.com/vinayakravi14/ROS_turtlebot_simple_planner.git
```
- Then build the package to enable roslaunch capabilities 
```
cd ~/<ROS_Workspace>/
catkin_make
```
- Move into the simple_controller/src and make scripts executable 
```
[For example]
chmod +x planner.py
chmod +x rotate.py
```
- Then launch the files in this step 
```
roslaunch simple_controller world.launch
python3 planner.py
python3 rotate.py
```
## Assumptions 
- The North Star is very close to Celestial North pole, so initially tracked to navigate to North pole 
- The World in Gazebo is following WSG84, hence the converted GPS local coordinate follows the same reference plane ( will work to change on the future versions)

## Limitations
- The tracking is not GPS-enabled, should publish a fake-gps or track the northpole with IMU
- Jumpy/Jittery movements which sometimes throws the tracker off-beat
- should solve that by probably deplying some kind-off control mechanism (controller or Kalman filter) 




