import numpy as np
import cv2

def order_points(pts):
    '''
        points are ordered:
        top-left
        top-right
        bottom-right
        bottom-left
    '''

    rect = np.zeros((4,2), dtype = 'float32')

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = pts.diff(axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect



if __name__ == '__main__':
    print('Starting the app')
