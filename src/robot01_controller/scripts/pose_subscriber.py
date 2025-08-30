#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo('(' + str(msg.x) + ', ' + str(msg.y) + ')')

if __name__ == '__main__':
    rospy.init_node('turtle_pose_subscriber')

    sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pose_callback)
                                                # function that the subscriber going to listen to the topic
    rospy.loginfo('Node has been started')
    
    rospy.spin()        # infinite loop, can exit with Ctrl+C
