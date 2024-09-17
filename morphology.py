# Import necessary libraries and packages
import numpy as np
import cv2
import os

class MorphologicalOperations:
    def __init__(self, image_path):

        # Initialize with the path to the image
        self.image_path= image_path
        self.image= cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale
        
    def erode(self, kernel_size= (5,5), iterations= 1):
        '''Apply erosion to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Create the kernel
        kernel= np.ones(kernel_size, np.uint8)
        
        # Apply erosion
        eroded_image= cv2.erode(self.image, kernel, iterations= iterations)
        return eroded_image
    
    def dilate(self, kernel_size= (5,5), iterations= 1):
        '''Apply dilation to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Create the kernel
        kernel= np.ones(kernel_size, np.uint8)

        # Apply dilation
        dilated_image= cv2.dilate(self.image, kernel, iterations= iterations)
        return dilated_image
    
    def opening(self, kernel_size= (5,5)):
        '''Apply opening to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Create the kernel
        kernel= np.ones(kernel_size, np.uint8)

        # Apply opening (erosion followed by dilation)
        opened_image= cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)
        return opened_image
    
    def closing(self, kernel_size= (5,5)):
        '''Apply closing to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Create the kernel
        kernel= np.ones(kernel_size, np.uint8)

        # Apply closing (dilation followed by erosion)
        closed_image= cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        return closed_image
    
# Testing the MorphologicalOperations class
if __name__ == '__main__':

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/blue_cap.jpg'

    # Path to save output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for MorphologicalOperations
    morph_ops= MorphologicalOperations(image_path)

    # Apply erosion
    eroded_image= morph_ops.erode()
    if eroded_image is not None:
        cv2.imshow('Eroded Image', eroded_image)
        cv2.imwrite(os.path.join(output_path, 'eroded_image.jpg'), eroded_image)
        cv2.waitKey(0)

    # Apply dilation
    dilated_image= morph_ops.dilate()
    if dilated_image is not None:
        cv2.imshow('Dilated Image', dilated_image)
        cv2.imwrite(os.path.join(output_path, 'dilated_image.jpg'), dilated_image)
        cv2.waitKey(0)

    # Apply opening
    opened_image= morph_ops.opening()
    if opened_image is not None:
        cv2.imshow('Opened Image', opened_image)
        cv2.imwrite(os.path.join(output_path, 'opened_image.jpg'), opened_image)
        cv2.waitKey(0)

    # Apply closing
    closed_image= morph_ops.closing()
    if closed_image is not None:
        cv2.imshow('Closed Image', closed_image)
        cv2.imwrite(os.path.join(output_path, 'closed_image.jpg'), closed_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()