import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2
import base64
from io import BytesIO
from PIL import Image

model = keras.models.load_model("mnist_model.h5")


def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data)).convert("L")
    image = np.array(image)
    return image


def predict_digit(base64_string):
    image = base64_to_image(base64_string)

    image = cv2.resize(image, (28, 28))
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)

    prediction = model.predict(image)
    predicted_digit = np.argmax(prediction)

    print(f"Tahmin Edilen Rakam: {predicted_digit}")

    plt.imshow(image.reshape(28, 28), cmap="gray")
    plt.title(f"AI Tahmini: {predicted_digit}")
    plt.show()

    return predicted_digit


base64_sample = "iVBORw0KGgoAAAANSUhEUgAA..."  # Buraya gerçek base64 string koy
predicted = predict_digit(base64_sample)
print("Model Tahmini:", predicted)
