import cv2
import numpy as np

image = cv2.imread("object.jpg")
if image is None:
    print("File not found!")
    exit()

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = clahe.apply(gray)


gray = cv2.GaussianBlur(gray, (5, 5), 0)


binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 0)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total_stars = 0

min_area = 0 
max_area = 500  
circularity_threshold = 0.3 

processed = [False] * len(contours)

for i, cnt in enumerate(contours):
    if processed[i]:
        continue

    area = cv2.contourArea(cnt)
    if area < min_area or area > max_area:
        continue

    perimeter = cv2.arcLength(cnt, True)
    if perimeter == 0:
        continue

    circularity = 4 * np.pi * area / (perimeter * perimeter)
    if circularity < circularity_threshold:
        continue

    total_stars += 1
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    processed[i] = True

print(f"Toplam Star Count: {total_stars}")

cv2.imshow("Detected Stars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
