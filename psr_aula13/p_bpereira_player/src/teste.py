#!/usr/bin/env python3

import rospy
from utilitario import configurarEquipa, configurarEstrategia

import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

import math
import tf.transformations
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from math import atan2, sqrt
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, LaserScan
import cv2
import numpy as np


def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)



def handle_image(msg):
    my_team = 'red'

    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")  # "passthrough" ) #

    cv2.imshow("red1", cv_image)

    green_mask = cv2.inRange(cv_image, (0, 100, 0), (50, 256, 50))
    red_mask = cv2.inRange(cv_image, (0, 0, 100), (50, 50, 256))
    blue_mask = cv2.inRange(cv_image, (100, 0, 0), (256, 50, 50))
    if my_team == 'blue':
        prey_mask = red_mask
        hunter_mask = green_mask
    elif my_team == 'red':
        prey_mask = green_mask
        hunter_mask = blue_mask
    elif my_team == 'green':
        prey_mask = blue_mask
        hunter_mask = red_mask

    # output_prey = cv2.connectedComponentsWithStats(prey_mask, connectivity=8)
    #
    # output_hunter = cv2.connectedComponentsWithStats(hunter_mask, connectivity=8)

    # print (output_prey)

    cv2.imshow("red1", cv_image)
    rospy.sleep(0.02)
    cv2.imshow("prey", prey_mask)
    rospy.sleep(0.02)
    cv2.imshow("hunter", hunter_mask)


def marcador(): # Funciona
    topic = 'visualization_marker_array'
    publisher = rospy.Publisher(topic, MarkerArray)

    # rospy.init_node('register')

    markerArray = MarkerArray()

    count = 0
    MARKERS_MAX = 100

    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "red1/base_link"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = math.cos(count / 50.0)
        marker.pose.position.y = math.cos(count / 40.0)
        marker.pose.position.z = math.cos(count / 30.0)

        # We add the new marker to the MarkerArray, removing the oldest marker from it when necessary
        if (count > MARKERS_MAX):
            markerArray.markers.pop(0)

        markerArray.markers.append(marker)

        # Renumber the marker IDs
        id = 0
        for m in markerArray.markers:
            m.id = id
            id += 1

        # Publish the MarkerArray
        publisher.publish(markerArray)

        count += 1

        rospy.sleep(0.01)


def listener():
    node_name = 'red1'



    rospy.Subscriber("/" + node_name +"/camera/rgb/image_raw", Image, handle_image)

    rospy.spin()


def main():


    node_name = 'red1'

    equipa = configurarEquipa(node_name)

    estrategia = configurarEstrategia('red')

    # rospy.init_node('driver', anonymous=False)

    print('+++++++++++++++++++++++++++++++++++++++')

    print (equipa['minhaquipa'])

    print('+++++++++++++++++++++++++++++++++++++++')

    print(estrategia)

    print('++++++++++++++++'+ str(estrategia['red2'])+'+++++++++++++++++++++++')

    # rospy.init_node('register')

    # marcador()

    # listener()




if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
