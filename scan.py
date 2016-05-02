'''
http://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
'''

from transform import four_point_transform
import imutils

from debug_utils import debug

from skimage.filters import threshold_adaptive
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()

ap.add_argument('-i', '--image', required=True,
        help='Path to the image to be scanned')

args = vars(ap.parse_args())

print(args)

# Edge Detection
# load the image and compute the ratio of the current height
# to the height we are going to resize it to.

image = cv2.imread(args['image'])
ratio = image.shape[0] / 500.0
orig = image.copy()

image = imutils.resize(image, height=500)

# convert to grayscale, blur the picture then find edges.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

print('Step 1: Edge Detection')

cv2.imshow('Image', image)
cv2.imshow('Edged', edged)

cv2.waitKey(0)
cv2.destroyAllWindows()

# find the contours of the the edged image. Since we know that
# the largest contours will be of the paper and that the paper
# will be a rectangle, we can keep only the largest 4 contours
# as our image.
im2, cnts, hierarchy = cv2.findContours(edged.copy(),
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

for c in cnts:

    # approximate the contour
    peri = cv2.arcLength(c, True)

    debug('peri', peri)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    debug('approx', approx)

    if len(approx) == 4:
        screenCnt = approx
        break


print('Step 2: Find Contours of paper')

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

cv2.imshow('Outlined', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

if __name__ == '__main__':
    print('lets go!')
