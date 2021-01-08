#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Twist
import math


roll = pitch = yaw = 0.0
target = 90
kp=0.5

def euler_to_quaternion(yaw, pitch, roll):
    
        qx = math.sin(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) - math.cos(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
        qy = math.cos(roll/2) * math.sin(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.cos(pitch/2) * math.sin(yaw/2)
        qz = math.cos(roll/2) * math.cos(pitch/2) * math.sin(yaw/2) - math.sin(roll/2) * math.sin(pitch/2) * math.cos(yaw/2)
        qw = math.cos(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)

        return [qx, qy, qz, qw]

def quaternion_to_euler(x, y, z, w):
    

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))

        return X, Y, Z
    
def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = quaternion_to_euler(orientation_list[0],orientation_list[1],orientation_list[2],orientation_list[3])
    print yaw

rospy.init_node('rotate_robot')

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
r = rospy.Rate(10)
command =Twist()

while not rospy.is_shutdown():
    #quat = quaternion_from_euler (roll, pitch,yaw)
    #print quat
    target_rad = target*math.pi/180
    command.angular.z = kp * (target_rad-yaw)
    pub.publish(command)
    print("taeget={} current:{}", target,yaw)
    r.sleep()