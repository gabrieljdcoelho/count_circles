import cv2
import numpy as np

def detect_circles(image):

    img = cv2.imread("data/" + image, 0)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,5,
                            param1=118,param2=8,minRadius=8,maxRadius=10)

    circles = np.uint16(np.around(circles))
    print(circles[0,:])
    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),1)

    #cv2.imshow('detected circles',cimg)
    cv2.imwrite("output/" + image + ".png", cimg)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return circles.shape[1]