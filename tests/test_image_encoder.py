import os
import pytest
import unittest
from PIL import UnidentifiedImageError
from app.image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../app"))
        self.test_files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_files"))

        # Example valid 360x360 image
        self.valid_image = os.path.join(self.app_dir, "img-1.jpeg")

        # Example wrong-size image
        self.wrong_size_image = os.path.join(self.test_files_dir, "ai-1.png")

        # Example invalid file types
        self.invalid_pdf = os.path.join(self.test_files_dir, "sample.pdf")
        self.invalid_docx = os.path.join(self.test_files_dir, "sample.docx")
        self.invalid_xlsx = os.path.join(self.test_files_dir, "sample.xlsx")

    def test_valid_image(self):
        """Valid 360x360 JPG/PNG should encode without exception"""
        try:
            self.processor.image_encode(self.valid_image)
        except ValueError:
            self.fail("image_encode() raised ValueError unexpectedly for valid image!")

    def test_wrong_dimensions(self):
        """Image with wrong dimensions should raise ValueError"""
        with self.assertRaises(ValueError) as context:
            self.processor.image_encode(self.wrong_size_image)
        self.assertIn("Image must be 360x360 pixels", str(context.exception))

    def test_invalid_file_types(self):
        """Non-image files should raise ValueError"""
        for invalid_file in [self.invalid_pdf, self.invalid_docx, self.invalid_xlsx]:
            with self.assertRaises(ValueError) as context:
                self.processor.image_encode(invalid_file)
            self.assertIn("Only JPG or PNG images are accepted", str(context.exception))

    def test_data_types(self):
        with self.assertRaises(TypeError):
            self.processor.image_encode(21341)

if __name__ == '__main__':
    unittest.main()
