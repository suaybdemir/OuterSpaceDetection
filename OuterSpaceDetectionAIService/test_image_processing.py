import unittest
import numpy as np
from process_image import base64_to_image

class TestImageProcessing(unittest.TestCase):
    def test_base64_to_image(self):
        base64_sample = "iVBORw0KGgoAAAANSUhEUgAA..."  # Gerçek base64 ekleyin
        image = base64_to_image(base64_sample)
        self.assertIsInstance(image, np.ndarray)

if __name__ == '__main__':
    unittest.main()
