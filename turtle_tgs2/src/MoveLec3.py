#! /usr/bin/env python

from __future__ import print_function

import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    #start new node
    rospy.init_node('turtle_mover', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("moving forward 1m")
    distance = 1
    speed = 0.5
    angle = 45
    angularspeed = 90
    #init
    vel_msg.linear.x = abs(speed) #speed of 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    
    while(current_distance < distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance= speed*(t1-t0)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

    print("rotating")
    #convert to radian
    
    angular_speed = angularspeed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.angular.z = -abs(angular_speed)
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
    
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()



if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass