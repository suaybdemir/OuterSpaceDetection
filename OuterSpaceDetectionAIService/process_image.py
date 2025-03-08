import cv2
import numpy as np

image = cv2.imread("object.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

color_ranges = {
    "Blue Star": (np.array([90, 50, 50]), np.array([130, 255, 255])),  # Blue Stars
    "Blue White Star": (np.array([100, 30, 200]), np.array([130, 70, 255])),  # Blue-White Stars
    "White Star": (np.array([0, 0, 200]), np.array([180, 30, 255])),  # White Stars
    "Yellow White Star": (np.array([20, 50, 200]), np.array([40, 150, 255])),  # Yellow-White Stars
    "Yellow Star": (np.array([15, 150, 150]), np.array([35, 255, 255])),  # Yellow Stars
    "Orange Star": (np.array([10, 150, 100]), np.array([25, 255, 255])),  # Orange Stars
    "Red Star": (np.array([0, 150, 50]), np.array([10, 255, 255])),  # Red Stars
    "mars": (np.array([0, 150, 100]), np.array([10, 255, 255])),  # Red Mars
    "jupiter": (np.array([15, 80, 100]), np.array([30, 255, 255])),  # Yellow Jupiter
    "meteors": (np.array([40, 50, 50]), np.array([80, 255, 255]))  # Green Meteors
}

object_counts = {}
object_centers = []

for obj_type, (lower, upper) in color_ranges.items():
    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    centers = []
    for cnt in contours:
        if cv2.contourArea(cnt) <= 50:  # Filter big noise
            x, y, w, h = cv2.boundingRect(cnt)
            cx, cy = x + w // 2, y + h // 2  # Get center
            centers.append([cx, cy])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1

    object_counts[obj_type] = count
    object_centers.extend(centers)

object_centers = np.array(object_centers)

print("Detected Objects:")
for obj, count in object_counts.items():
    print(f"- {obj.capitalize()}: {count}")


cv2.imshow("Detected Space Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
