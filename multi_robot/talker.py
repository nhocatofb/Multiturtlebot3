import rospy
from geometry_msgs.msg import Twist
from math import pi


def talker():
    pub = rospy.Publisher("tb3_0/cmd_vel", Twist, queue_size=100)
    pub2 = rospy.Publisher("tb3_1/cmd_vel", Twist, queue_size=100)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate(1)
    speed = 0.2
    count = 0
    while not rospy.is_shutdown():
        message = Twist()
        message.linear.x = speed
        pub.publish(message)
        pub2.publish(message)
        count+=1
        if count == 3: 
        	speed *= -1
        	count = 0
        rate.sleep()


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
