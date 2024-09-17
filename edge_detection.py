# Import necessary libraries and packages
import os
import cv2

class EdgeDetection:
    def __init__(self, image_path):

        # Initialize with the path to the image
        self.image_path= image_path
        self.image= cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale

    def canny_edge_detection(self, threshold1= 100, threshold2= 200):
        '''Apply Canny Edge Detection to the image'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Apply Canny Edge Detection
        edges= cv2.Canny(self.image, threshold1, threshold2)
        return edges
    
# Testing the EdgeDetection class
if __name__ == '__main__':

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test.jpg'

    # Path to save the output image
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for EdgeDetection
    edge_detector= EdgeDetection(image_path)

    # Apply Canny Edge Detection
    canny_edges= edge_detector.canny_edge_detection()
    if canny_edges is not None:
        cv2.imshow('Canny Edge Detection', canny_edges)
        cv2.imwrite(os.path.join(output_path, 'canny_edge_image.jpg'), canny_edges)
        cv2.waitKey(0)

    cv2.destroyAllWindows()