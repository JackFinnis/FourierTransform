import cv2
import numpy as np

def getContour(imgName):
    img = cv2.imread(imgName)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]

    img = np.zeros(img.shape)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
    cv2.imwrite('contours.jpg', img)

    return max(contours, key = cv2.contourArea).squeeze()

def getPath(imgName):
    contour = getContour(imgName)
    return [complex(x[0], x[1]) for x in contour]


def oldGetContour(imgName):
    img = cv2.imread(imgName)
    scale = 1000 / max(img.shape)
    newHeight = int(img.shape[0] * scale)
    newWidth = int(img.shape[1] * scale)
    imgScaled = cv2.resize(img, (newWidth, newHeight))
    imgBinary = cv2.cvtColor(imgScaled, cv2.COLOR_BGR2GRAY)

    imgBilat = cv2.bilateralFilter(imgBinary, 10, 10, 10)
    imgEdged = cv2.Canny(imgBilat, 100, 200)
    cv2.imwrite('edges.jpg', imgEdged)

    thresh = 75
    imgFlip = cv2.flip(imgBinary, 0)
    ret, threshImg = cv2.threshold(imgFlip, thresh, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(threshImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    imgZeros = np.zeros(imgScaled.shape)
    cv2.drawContours(imgZeros, contours, -1, (0, 255, 0), 1)
    imgFlip = cv2.flip(imgZeros, 0)
    cv2.imwrite('contours.jpg', imgFlip)

    return max(contours, key = len).squeeze()

    # scaled = imutils.resize(img, 1000)
    # blur = cv2.blur(gray, (5, 5), 0)
    # canny = cv2.Canny(blur, 0, 255)

    # thresh = cv2.erode(thresh, None, iterations = 2)
    # thresh = cv2.dilate(thresh, None, iterations = 2)
    
    # cv2.imwrite('canny.jpg', canny)
    