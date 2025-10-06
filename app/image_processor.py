"""
Document: image_processor.py
Function: Module for processing image such as encoding it to binaries or decoding binaries into image.
Author: PURA, Joshua Elijah L.
Date Created: October 6, 2025
Date Updated: October 6, 2025
Version: 0.0.1
"""
from PIL import Image
import numpy as np

class ImageProcessor:
    __HEIGHT = 360
    __WIDTH = 360
    __CHANNELS = 3

    @staticmethod
    def __image_encoder(image):
        """
        Function: __image_encoder(image)
        Description: This private function accept a file path then locate that file path, open and read it, then
                     encode it into a binary file.
        Arguments:
            image (string): Path to the image to be encoded.
        Returns:
            hex_array: An array of encoded bytes of the image.
        Raises:
            > Accepts different files such as pdf, word, xslx. It should only accept jpg.
            > Accepts different dimension of image. It should only accept 360 x 360 pixels image.
            
        """
        img = Image.open(image).convert("RGB")
        img_array = np.array(img)
        img_bytes = img_array.tobytes()
        hex_array = np.apply_along_axis(lambda pixel: "{:02x}{:02x}{:02x}".format(*pixel), 2, img_array)
        # For Debug Logging
        """
        for row in hex_array:
        print(" ".join(row))
        """

        with open("img.bin", "wb") as file:
            file.write(img_bytes)
        return hex_array

    @staticmethod
    def __image_decoder(bin):
        """
        Function: __image_decoder(bin)
        Description: This private function decode a hex encoded binary file into an image.
        Arguments:
            bin(string): Binary encoded image.
        Returns:
            reconstructed_image (image): Reconstructed image from binary encoded image.
        Raises:
            no error detected yet.
        """
        with open(bin, "rb") as file:
            img_bytes = file.read()
            img_array = np.frombuffer(img_bytes, dtype=np.uint8)
            img_array = img_array.reshape((ImageProcessor.__HEIGHT, ImageProcessor.__WIDTH, ImageProcessor.__CHANNELS))

        reconstructed_image = Image.fromarray(img_array)
        reconstructed_image.show()

    def image_encode(self, image):
        """
        Function: image_encode(image)
        Description: This public function serves as the getter of the private __image_encoder function.
        Arguments:
        self (ImageProcessor): Image processor instance.
        image (string): Path to the image to be encoded.
        Returns:
            nothing.
        Raises:
            no error detected yet.
        """
        self.__image_encoder(image)

    def image_decode(self, binary):
        """
        Function: image_decode(binary)
        Description: This public function serves as the getter of the private __image_decoder function.
        Arguments:
        self (ImageProcessor): Image processor instance.
        binary (string): Binary encoded image.
        Returns:
             nothing.
        Raises:
            no error detected yet.
        """
        self.__image_decoder(binary)
