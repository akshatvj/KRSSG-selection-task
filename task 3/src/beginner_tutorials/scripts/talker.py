#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import time
class move:
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose = Pose()
        self.pose_sub =rospy.Subscriber('/turtle1/pose',Pose,self.upose)
        self.rate = rospy.Rate(50)
        print("init called")
        #self.pose.x = 3
        #self.pose.y = 5.4
        self.f = open("points.txt", "r")
        self.v=Pose()
    def upose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
    def gettar(self):
        tar = Pose()
        tar.x = float(self.f.readline())
        tar.y = float(self.f.readline())
        return tar
    def dist(self,p):
        s = sqrt(pow(p.x-self.pose.x,2) +(pow(p.y-self.pose.y,2)))
        return s
    def setv(self,p):
        cont = 0.9
        return  cont*self.dist(p)
    def pub(self):
        msg = Twist()
        v = self.gettar()
        while True:
            msg.linear.x = self.setv(v)
            msg.linear.y = 0
            msg.linear.z = 0
            msg.angular.x = 0
            msg.angular.y = 0
            msg.angular.z = 6*(self.steering_angle(v) - self.pose.theta)
            self.velocity_publisher.publish(msg)
            if(msg.linear.x<0.2 and msg.angular.z <0.9):
                v = self.gettar()
            self.rate.sleep()
x1 = move()
if __name__ == '__main__':
    x1.pub()
    rospy.spin()




