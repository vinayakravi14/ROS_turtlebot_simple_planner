#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import rospkg
import geonav_conversions


# function to convert file into array
def converter(file):
    for i in range(len(file)):
        file[i] = file[i].split(',')

    return file


# function to run turtlebot3
def runner(order):

    # declaring object for class Twist
    msg = Twist()

    # for i in range(len(order)):
    rate = rospy.Rate(2)

    msg.linear.x = float(orders[0])
    msg.linear.y = float(orders[1])
    msg.angular.z = 0

    rospy.loginfo(msg)
    pub.publish(msg)

    rate.sleep()


if __name__ == '__main__':

    global pub

    # publisher object publishing to command velocity
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # initialize node
    rospy.init_node('planner', anonymous=True)

    # read text file
    ros_root = rospkg.RosPack()
    # with open(ros_root.get_path('a-star-turtlebot') + '/output_files/commander_2.txt', 'r') as command:
    #     orders = command.readlines()
        
    # # convert into array
    # orders = converter(orders)
    orders = geonav_conversions.ll2xy(90.0,0,0,0)
    print ("[ALERT] ",orders)

    while True:
        # calling runner

        runner(orders)

    # runnning infinte times
    # rospy.spin()
