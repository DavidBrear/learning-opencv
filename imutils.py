import cv2

def showimg(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

def resize(image, target_size=100):

    r = float(scale) / image.shape[1]
    dim = (scale, int(image.shape[0] * r))

    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized

# rotate

def rotate(image, deg=90):

    (h, w) = image.shape[:2]
    center = (w/2, h/2)

    M = cv2.getRotationMatrix2D(center, deg, 1.0)

    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated

def crop(image, box):
    cropped = image[box]

    return cropped

