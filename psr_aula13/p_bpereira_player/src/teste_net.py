#!/usr/bin/env python3
import argparse

import colorama
import cv2
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def handle_image(msg):

    my_team = 'red'
    debugmode = True

    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")  #  "passthrough" ) #

   # cv2.imshow("red1", cv_image)

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

    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(prey_mask, connectivity=4)

    # Find the largest non background component.
    # Note: range() starts from 1 since 0 is the background label.
    max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA]) for i in range(1, nb_components)], key=lambda x: x[1])

    # print (max_label) 1
    # print (max_size) 277

    contoursm, _ = cv2.findContours(prey_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contoursmi in contoursm:
        M = cv2.moments(contoursmi)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            if debugmode:
                cv2.putText(cv_image, "presa", (cx , cy ), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    contoursm, _ = cv2.findContours(hunter_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contoursmi in contoursm:
        M = cv2.moments(contoursmi)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            if debugmode:
                cv2.putText(cv_image, "cacador", (cx , cy ), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("red1", cv_image)
    # rospy.sleep(0.02)
    # cv2.imshow("prey", prey_mask)
    # rospy.sleep(0.02)
    # cv2.imshow("hunter", hunter_mask)


def main():

    node_name = 'red1'

    rospy.init_node('driver', anonymous=False)
    rate = rospy.Rate(15)  # 10hz

    while True:
        bridge = CvBridge()
        rospy.Subscriber("/" + node_name + "/camera/rgb/image_raw",  Image, handle_image)

        if cv2.waitKey(1) == ord('q'):
            break

        rate.sleep()

        rospy.spin()

  #  capture.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
