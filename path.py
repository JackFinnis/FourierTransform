import cv2

def getContour(imgName):
    img = cv2.imread(imgName)
    imgFlip = cv2.flip(img, 0)
    imgBinary = cv2.cvtColor(imgFlip, cv2.COLOR_BGR2GRAY)
    thresh = 100

    ret, threshImg = cv2.threshold(imgBinary, thresh, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(threshImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return contours[0].squeeze()

def convertComplex(contour):
    compPoints = []
    for point in contour:
        compPoints.append(complex(point[0], point[1]))
    return compPoints

def getPath(imgName):
    contour = getContour(imgName)
    return convertComplex(contour)


# img_contours = np.zeros(img.shape)
# cv2.drawContours(img_contours, contours, -1, (0,255,0), 1)
# cv2.imwrite('new_img.png',img_contours)