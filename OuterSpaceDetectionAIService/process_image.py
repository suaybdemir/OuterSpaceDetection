import cv2
import numpy as np

image = cv2.imread("object.jpg")
if image is None:
    print("File not Found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.equalizeHist(gray)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 5
params.maxArea = 50

params.filterByCircularity = True
params.minCircularity = 0.3

params.filterByInertia = False
params.filterByConvexity = False

params.minThreshold = 10
params.maxThreshold = 200

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(gray)
total_stars = len(keypoints)
print(f"Total Star Count: {total_stars}")

im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Detected Stars", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
