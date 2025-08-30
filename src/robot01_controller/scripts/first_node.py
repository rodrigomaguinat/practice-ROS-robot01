#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')    # node name (test_node)   # executable name  (first_node) 
    rospy.loginfo('Test node has been started.')

    rate = rospy.Rate(10)   # 10 heads - 0.1 second (frecuency)

    while not rospy.is_shutdown():      # if it receive a signal will kill the loop
        rospy.loginfo('Hello')
        rate.sleep()        # to control the speed of the loop
