# Import necessary libraries and packages
import os
import cv2

class ImageSmoothing:
    def __init__(self, image_path):

        # Initialize with the path to the image
        self.image_path= image_path
        self.image= cv2.imread(self.image_path)

    def average_blur(self, kernel_size= (5,5)):
        '''Apply Averaging Blur to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Apply Averaging Blur
        blurred_image= cv2.blur(self.image, kernel_size)
        return blurred_image
    
    def gaussian_blur(self, kernel_size= (5,5), sigmaX= 0):
        '''Apply Gaussian Blur to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Apply Gaussian Blur
        gaussian_blurred_image= cv2.GaussianBlur(self.image, kernel_size, sigmaX)
        return gaussian_blurred_image
    
    def median_blur(self, kernel_size= 5):
        '''Apply Median Blur to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Apply Median Blur
        median_blurred_image= cv2.medianBlur(self.image, kernel_size)
        return median_blurred_image
    
    def bilateral_blur(self, d= 9, sigmaColor= 75, sigmaSpace= 75):
        '''Apply Bilateral Filter to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Apply Bilateral Filter
        bilateral_filtered_image= cv2.bilateralFilter(self.image, d, sigmaColor, sigmaSpace)
        return bilateral_filtered_image

# Testing the ImageSmoothing class
if __name__ == '__main__':

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test.jpg'

    # Path to save the output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for ImageSmoothing
    smoothing= ImageSmoothing(image_path)

    # Apply Average Blur
    averaged_image= smoothing.average_blur()
    if averaged_image is not None:
        cv2.imshow('Averaging Blur', averaged_image)
        cv2.imwrite(os.path.join(output_path, 'averaged_image.jpg'), averaged_image)
        cv2.waitKey(0)

    # Apply Gaussian Blur
    gaussian_blurred_image= smoothing.gaussian_blur()
    if gaussian_blurred_image is not None:
        cv2.imshow('Gaussian Blur', gaussian_blurred_image)
        cv2.imwrite(os.path.join(output_path, 'gaussian_blurred_image.jpg'), gaussian_blurred_image)
        cv2.waitKey(0)

    # Apply Median Blur
    median_blurred_image= smoothing.median_blur()
    if median_blurred_image is not None:
        cv2.imshow('Median Blur', median_blurred_image)
        cv2.imwrite(os.path.join(output_path, 'median_blurred_image.jpg'), median_blurred_image)
        cv2.waitKey(0)

    # Apply Bilateral Filter
    bilateral_filtered_image= smoothing.bilateral_blur()
    if bilateral_filtered_image is not None:
        cv2.imshow('Bilateral Filter', bilateral_filtered_image)
        cv2.imwrite(os.path.join(output_path, 'bilateral_filtered_image.jpg'), bilateral_filtered_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()