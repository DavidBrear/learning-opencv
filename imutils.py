import cv2

def showimg(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)

def resize(image, **kwargs):

    height = kwargs.get('height')
    width = kwargs.get('width')

    if height and not width:
        r = float(height) / image.shape[0]
        dim = (int(image.shape[1] * r), height)
    elif width and not height:
        r = float(width) / image.shape[1]
        dim = (width, int(image.shape[0] * r))
    else:
        dim = (int(width), int(height))

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

