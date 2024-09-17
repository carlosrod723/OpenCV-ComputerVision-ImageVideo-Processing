# Import necessary libraries and packages
import os
import numpy as np
import cv2

class ColorSpaces:
    def __init__(self, image_path):

        #Initialize with the path to the image
        self.image_path= image_path
        self.image= cv2.imread(self.image_path)

    def convert_bgr_to_gray(self):
        '''Convert the image from BGR to Grayscale'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Converting BGR to Grayscale
        gray_image= cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return gray_image
    
    def convert_bgr_to_hsv(self):
        '''Conver the image from BGR to HSV'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Converting BGR to HSV
        hsv_image= cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return hsv_image
    
    def track_color(self, lower_bound, upper_bound):
        '''Track a specific color in the image using HSV color space'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Convert BGR to HSV
        hsv_image= cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Create a mask for the color within the specified bounds
        mask= cv2.inRange(hsv_image, lower_bound, upper_bound)

        # Bitwise-AND mask and original image
        tracked_image= cv2.bitwise_and(self.image, self.image, mask= mask)
        return tracked_image

# Testing the ColorSpaces class
if __name__ == '__main__':

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/blue_cap.jpg'

    # Path to save the output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for ColorSpaces
    color_spaces= ColorSpaces(image_path)

    # Convert to Grayscale
    gray_image= color_spaces.convert_bgr_to_gray()
    if gray_image is not None:
        cv2.imshow('Grayscale Image', gray_image)
        cv2.imwrite(os.path.join(output_path, 'grayscale_image.jpg'), gray_image)
        cv2.waitKey(0)

    # Convert to HSV
    hsv_image= color_spaces.convert_bgr_to_hsv()
    if hsv_image is not None:
        cv2.imshow('HSV Image', hsv_image)
        cv2.imwrite(os.path.join(output_path, 'hsv_image.jpg'), hsv_image)
        cv2.waitKey(0)

    # Track the color blue in HSV
    lower_blue= np.array([100,150,0]) # Lower bound
    upper_blue= np.array([140,255,255]) # Upper bound
    tracked_image= color_spaces.track_color(lower_blue, upper_blue)
    if tracked_image is not None:
        cv2.imshow('Tracked Blue Color', tracked_image)
        cv2.imwrite(os.path.join(output_path, 'tracked_blue_color.jpg'), tracked_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()