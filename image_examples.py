import cv2

image = cv2.imread('./images/jurassic-park-tour-jeep.jpg')

def showimg(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

# show original

showimg('original', image)

# resize


r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
showimg('resized', resized)

# rotate

(h, w) = image.shape[:2]
center = (w/2, h/2)

M = cv2.getRotationMatrix2D(center, 180, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))
showimg('rotated', rotated)

