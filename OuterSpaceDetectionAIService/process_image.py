import cv2
image = cv2.imread("object.jpg")

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = clahe.apply(gray)

_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

processed = [False] * len(contours)

total_stars = 0

threshold = 0.01 # Potent Threshold for Little Stars
max_area = 500
step = 0.01

while threshold <= max_area:
    for i, cnt in enumerate(contours):
        if not processed[i]:
            area = cv2.contourArea(cnt)

            if area < threshold:
                total_stars += 1
                processed[i] = True
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    threshold += step 

print(f"Toplam Yıldız Sayısı: {total_stars}")

cv2.imshow("Detected Stars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
