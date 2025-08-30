#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')    # node name (test_node)   # executable name  (first_node)
    
    rospy.loginfo('Hello from test node')
    rospy.logwarn('This is a warning')
    rospy.logerr('This is an error')
    
    rospy.sleep(1.0)    # 1 second

    rospy.loginfo('End of program')