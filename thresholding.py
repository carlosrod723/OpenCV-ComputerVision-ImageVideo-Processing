# Import neccessary libraries and packages
import os
import cv2

class ImageThresholding:
    def __init__(self, image_path):
        
        # Initialize with the path to the image
        self.image_path= image_path
        self.image= cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale

    def simple_threshold(self, threshold_value= 127, max_value= 255):
        '''Aply simple thresholding to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Applying simple thresholding
        _, thresholded_image= cv2.threshold(self.image, threshold_value, max_value, cv2.THRESH_BINARY)
        return thresholded_image
    
    def adaptive_threshold(self, max_value= 255, adaptive_method= cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                           threshold_type= cv2.THRESH_BINARY, block_size= 11, C= 2):
        '''Apply adaptive thresholding to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Applying adaptive thresholding
        adaptive_thresh_image= cv2.adaptiveThreshold(self.image, max_value, adaptive_method, threshold_type, block_size, C)
        return adaptive_thresh_image
    
    def otsu_threshold(self):
        '''Apply Otsu's Binarization to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Applying Otsu's thresholding
        _, otsu_thresh_image= cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return otsu_thresh_image
    
# Testing the ImageThresholding class
if __name__== '__main__':

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/blue_cap.jpg'

    # Path to save the output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for image thresholding
    thresholding= ImageThresholding(image_path)

    # Apply simple thresholding
    simple_thresh_image= thresholding.simple_threshold()
    if simple_thresh_image is not None:
        cv2.imshow('Simple Thresholding', simple_thresh_image)
        cv2.imwrite(os.path.join(output_path, 'simple_threshold_image.jpg'), simple_thresh_image)
        cv2.waitKey(0)

    # Apply adaptive thresholding
    adaptive_thresh_image= thresholding.adaptive_threshold()
    if adaptive_thresh_image is not None:
        cv2.imshow('Adaptive Thresholding', adaptive_thresh_image)
        cv2.imwrite(os.path.join(output_path, 'adaptive_threshold_image.jpg'), adaptive_thresh_image)
        cv2.waitKey(0)

    # Apply Otsu's thresholding
    otsu_thresh_image= thresholding.otsu_threshold()
    if otsu_thresh_image is not None:
        cv2.imshow('Otsu Thresholding', otsu_thresh_image)
        cv2.write(os.path.join(output_path, 'otsu_threshold_image.jpg'), otsu_thresh_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
