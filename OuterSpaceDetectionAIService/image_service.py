from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/detect-stars", methods=["POST"])
def detect_stars():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    image = cv2.imread(filepath)
    if image is None:
        return jsonify({"error": "Invalid image file"}), 400
    
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
    
    return jsonify({"total_stars": total_stars})

@app.route("/detect-stars-fast", methods=["POST"])
def detect_stars_fast():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    image = cv2.imread(filepath)
    if image is None:
        return jsonify({"error": "Invalid image file"}), 400
    
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
        processed[i] = True
    
    return jsonify({"total_stars": total_stars})

if __name__ == "__main__":
    app.run(debug=True)
